import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

def generate_ambient_drone():
    sample_rate = 48000
    # 64 seconds = exactly 8 cycles of 8-second swells -> perfectly loopable
    duration = 64.0
    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)

    # 1. Fundamental Frequencies (A minor - Open Fifth: A and E)
    # A0 = 27.5 Hz (sub-bass vibration)
    # A1 = 55.0 Hz (bowed double bass root)
    # E2 = 82.41 Hz (open fifth lower)
    # A2 = 110.0 Hz (pad body)
    # E3 = 164.81 Hz (open fifth upper)

    f_A0 = 27.5
    f_A1 = 55.0
    f_E2 = 82.4069
    f_A2 = 110.0
    f_E3 = 164.8138

    # 2. Bowed Double Bass Synthesis (Low A1 + subtle warmth)
    # Combining fundamental sine with gentle warm odd/even harmonics for friction texture
    bass = (
        0.55 * np.sin(2 * np.pi * f_A1 * t) +
        0.25 * np.sin(2 * np.pi * (f_A1 * 2) * t) +
        0.12 * np.sin(2 * np.pi * (f_A1 * 3) * t) +
        0.06 * np.sin(2 * np.pi * (f_A1 * 4) * t) +
        0.30 * np.sin(2 * np.pi * f_A0 * t)  # Sub weight
    )

    # Add subtle bowed friction noise (filtered brownian noise)
    noise = np.random.normal(0, 1, num_samples)
    sos_noise = butter(4, 180, 'lp', fs=sample_rate, output='sos')
    bow_friction = sosfilt(sos_noise, noise) * 0.04
    bass += bow_friction

    # 3. Open Fifth: E2 & E3
    fifth = (
        0.40 * np.sin(2 * np.pi * f_E2 * t) +
        0.20 * np.sin(2 * np.pi * f_E3 * t)
    )

    # 4. Warm Analog Pad (Detuned Oscillators for lush, warm chorus effect)
    # Stereo detuning
    detune = 0.25  # cents/Hz detune
    pad_left = (
        0.30 * np.sin(2 * np.pi * (f_A2 - detune) * t) +
        0.25 * np.sin(2 * np.pi * (f_E3 + detune * 1.5) * t) +
        0.15 * np.sin(2 * np.pi * (f_A1 * 2.005) * t)
    )
    pad_right = (
        0.30 * np.sin(2 * np.pi * (f_A2 + detune) * t) +
        0.25 * np.sin(2 * np.pi * (f_E3 - detune * 1.5) * t) +
        0.15 * np.sin(2 * np.pi * (f_A1 * 1.995) * t)
    )

    # 5. Slow swells roughly every 8 seconds (Period T = 8.0s, f = 1/8 = 0.125 Hz)
    # Using raised cosine for smooth, breathing swell (ranging between 0.65 and 1.0)
    swell = 0.825 + 0.175 * np.cos(2 * np.pi * (1.0 / 8.0) * t - np.pi)

    # Secondary micro-swell (breathing texture, 16s cycle)
    micro_swell = 0.90 + 0.10 * np.cos(2 * np.pi * (1.0 / 16.0) * t)

    total_swell = swell * micro_swell

    # Combine channels
    left = (bass * 0.7 + fifth * 0.5 + pad_left * 0.6) * total_swell
    right = (bass * 0.7 + fifth * 0.5 + pad_right * 0.6) * total_swell

    # 6. Warm Analog Low-pass Filter (leaving upper frequencies clean for narrator)
    # 4th order low-pass at 420 Hz to eliminate harshness and leave 1-4kHz open for voice
    sos_warm = butter(4, 420, 'lp', fs=sample_rate, output='sos')
    left = sosfilt(sos_warm, left)
    right = sosfilt(sos_warm, right)

    # 7. Ensure perfect seamless looping (crossfade 1.0s at boundary)
    fade_len = int(sample_rate * 1.0)
    fade_in = np.linspace(0, 1, fade_len)
    fade_out = np.linspace(1, 0, fade_len)
    
    # Overlap tail into head for seamless loop
    left[:fade_len] = left[:fade_len] * fade_in + left[-fade_len:] * fade_out
    right[:fade_len] = right[:fade_len] * fade_in + right[-fade_len:] * fade_out
    
    # Trim to exactly 64 seconds
    left = left[:num_samples]
    right = right[:num_samples]

    # Normalize to -3 dB peak to avoid clipping
    stereo = np.vstack((left, right))
    max_val = np.max(np.abs(stereo))
    target_peak = 0.7079  # -3 dBFS
    stereo = (stereo / max_val) * target_peak

    # Convert to 16-bit PCM WAV
    audio_int16 = (stereo.T * 32767).astype(np.int16)

    output_path = "public/audio/kanto-001-bulbasaur/ambient-drone.wav"
    wavfile.write(output_path, sample_rate, audio_int16)
    print(f"Successfully generated ambient underscore: {output_path} (Duration: {duration}s, 48kHz Stereo)")

if __name__ == "__main__":
    generate_ambient_drone()
