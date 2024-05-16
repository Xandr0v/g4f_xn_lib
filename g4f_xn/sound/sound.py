METAL_PIPE = 'g4f_xn/sound/metal-pipe.wav'
COINS = 'g4f_xn/sound/coins.wav'
HINT = 'g4f_xn/sound/Hint.wav'
RAND_SOUND_KWARGS = {'add_vol': (-25, -21), 'speed': (0.9, 1.1), 'pause': (0.2, 0.6)}


def _speed_change(sound, speed):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


def _sound_one(src, add_vol=0, speed=1.0, reverse=False):
    from pydub import AudioSegment
    from pydub.playback import play
    s = AudioSegment.from_wav(src) + add_vol
    s = _speed_change(s, speed)
    if reverse:
        s = s.reverse()
    play(s)


_irange = tuple[int, int]
_frange = tuple[float, float]


def sound(src=HINT,
          add_vol: int | _irange = 0,
          speed: float | _frange = 1.0,
          pause: float | _frange | None = None,
          reverse=False):

    import threading, time
    from random import uniform, randint

    av = add_vol if type(add_vol) is int else randint(*add_vol)
    s = speed if type(speed) is float else uniform(*speed)


    if pause is not None:
        p = pause if type(pause) is float else uniform(*pause)
        t = threading.Thread(target=_sound_one, args=(src, av, s))
        t.start()
        time.sleep(p)
    else:
        _sound_one(src, av, s)




def secret():
    from ..test_providers import (gr, d)

    print(f'{gr}Su', end='')
    sound(COINS, **RAND_SOUND_KWARGS)
    print(f'cce', end='')
    sound(COINS, **RAND_SOUND_KWARGS)
    print(f'ss{d}')
    sound(COINS, **RAND_SOUND_KWARGS)
