from g4f import ChatCompletion, Provider
from colorama import Fore
from functools import cache
from g4f_xn.misc import *




auth = {}


@cache
def c(color: str):
    return getattr(Fore, ("LIGHT%s_EX" % color).upper())

cy = c('cyan')
bl = c('blue')
rd = c('red')
yl = c('yellow')
gr = c('green')
mg = c('magenta')
wh = c('white')
d = Fore.RESET






def test_completion(provider, model, prompt, auth):
    return ChatCompletion.create(
            provider=provider,
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
                ],
            auth=auth
            )




def get_providers() -> list:
    providers = []
    ps = [a for a in dir(Provider) if not a.startswith('__') and a != 'Provider' and a != 'Providers']
    for p in ps:
        provider = getattr(Provider, p)


        if "create_completion" in dir(provider) and \
                "models" in dir(provider) and \
                isinstance(getattr(provider, "models"), (str, list)):
            providers.append(provider)

    return providers



def test_providers(*skip, show_failed=True, prompt='hello'):
    cnt_resp = 0
    cnt_error = 0
    cnt_skip = 0
    working_providers = []
    for provider in get_providers():
        provider_name = provider.__name__.split(".")[-1]
        models = [provider.models] if isinstance(provider.models, str) else provider.models

        if not provider.working:
            print(f'{rd}provider {repr(provider_name)} is not working{d}\n')
            continue

        if len(models) == 0 and show_failed:
            print(f'{bl}provider {d}{repr(provider_name)}{bl} has no available models{d}\n')
            continue

        print(f'{bl}Testing provider {d}{repr(provider_name)}\n')

        for model in models:

            if provider_name in skip:
                cnt_skip += 1

                print(f'\tmodel {repr(model)} was skipped\n')
                continue

            try:
                response = test_completion(provider, model, prompt, auth.get(provider_name))
                cnt_resp += 1

                print(f'\t{bl}model {gr}{repr(model)}{bl} responded:{d}')
                print(f'\t{cy}{cut(response.replace('\n', r'\n'), 100)}{d}\n')
                working_providers.append(f'{gr}{repr(provider_name)} - {repr(model)}{d}')

            except (KeyboardInterrupt, EOFError):

                print(f'{yl}test interrupted{d}')
                return
            except BaseException as e:
                cnt_error += 1
                if show_failed:
                    print(f'\t{bl}model {d}{repr(model)}{bl} failed with exception:{d}')
                    print(f'\t{rd}{type(e).__name__}: {cut(str(e).replace('\n', r'\n'), 100)}{d}\n')

    result = f'{mg}{cnt_resp} responded{d} | {rd}{cnt_error} failed{d}'
    if cnt_skip > 0:
        result = f'{mg}{cnt_resp} responded{d} | {rd}{cnt_error} failed{d} | {yl}{cnt_skip} skipped{d}'
    print(f'{gr}Test completed.{d} ( {result} )')
    print('working providers:')
    for p in working_providers:
        print(f'\t{p}')