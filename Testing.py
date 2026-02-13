import ollama

def velgModel(spørring):
    response = ollama.chat(model='llama3.2', 
                           messages=[{'role': 'user', 
                                      'content': 'your job is to be a judge, based on the content of the '
                                      'question given to you respond with one word about witch categori '
                                      'the question best fits into. '
                                      'the options are as follows: '
                                      'Coding, Simple-question, Advanced-question, Internet-search. The question is: ' + spørring}])
    print(response['message']['content'])


velgModel("What is the capital of France?")