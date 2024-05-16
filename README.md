### g4f_xn

---
#### A library that allows you to use different GPT models!

Also has some other stuff like:
- reading and writing to files
- sound playback(i mean why not)
- other functions for convenience

The project is not ready for public use, but more for a fun and convinient (in my opinion) use of gpt models 

#### code example:

```python
import g4f_xn

# specify model
g4f_xn.settings('gpt-3.5-turbo')

prompt = '''
type numbers from 1 to 10
'''

result = g4f_xn.gpt(prompt)
print(result)
```

---
also you can provide an array to xn.gpt that will represent history of previous prompts and answers. It will use it as context and append prompt with response.


#### advanced example:

```python
import g4f_xn

# specify model and provider
g4f_xn.settings('gpt-4', 'Bing')

p1 = '''
type numbers from 1 to 10
'''
p2 = '''
multiply each number by 2
'''

chat = []

r1 = g4f_xn.gpt(p1, chat)
r2 = g4f_xn.gpt(p2, chat)
print(r1)  # 1, 2, 3, ...
print(r2)  # 2, 4, 6, ...
```
---

#### gpt -> chat gpt
You can also save chat variable to txt file using xn.write, xn.read <br>
it will be basically chatgpt now

#### example with local chat history:

```python
import g4f_xn

g4f_xn.settings('gpt-3.5-turbo')

history = g4f_xn.read(r'path/to/file.txt')
chat = [history]
prompt = '''
type numbers from 1 to 10
'''

result = g4f_xn.gpt(prompt, chat)
print(result)

g4f_xn.write(''.join(chat), r'path/to/file.txt')
```
---
It is highly recommended to use .ipynb files with this library as it is really flexible for that task


