import tkinter as tk

janela = tk.Tk()

janela.title('RPG FODA')
janela.geometry('800x600')

#texto inicial de teste e apresentação
texto_inicial=tk.Label(
    janela,
    text='Voce está prestes a entrar em um mundo de ilusao e fantasia. Se prepare' \
    'aqui a chapa é quente e qualquer coisa pode te matar, qualquer coisa mesmo.' \
    'Te matar....ou te salvar.',
    wraplength=600,
    justify='center',
    font=('Arial',14)
)

texto_inicial.pack(pady=20)


#loop do jogo
janela.mainloop()