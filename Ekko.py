import ollama

def velgOppgaveType(spørring):
    response = ollama.chat(model='llama3.2', 
                           messages=[{'role': 'user', 
                                      'content': 'your job is to be a judge, based on the content of the '
                                      'question given to you respond with one word about witch categori '
                                      'the question best fits into. '
                                      'the options are as follows: '
                                      'Coding, Simple-question, Advanced-question, Internet-search. The question is: ' + spørring}])
    print(response['message']['content'])




def startchat():
    messages = []  # keeps chat history
    while True:
        inp = input("</> ")

        if inp.lower() in ("exit", "quit"):
            break

        velgOppgaveType(inp)


def velgModell(oppgaveType):
    if oppgaveType == "Coding":
        return "code-davinci-002"
    
    elif oppgaveType == "Simple-question":
        return "text-davinci-003"
    
    elif oppgaveType == "Advanced-question":
        return "text-davinci-003"
    
    elif oppgaveType == "Internet-search":
        return "text-davinci-003"
    
    else:
        return "text-davinci-003"  # default model



startchat()