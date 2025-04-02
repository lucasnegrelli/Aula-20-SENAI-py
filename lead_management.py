import sqlite3  # banco de dados
import tkinter as tk  # interface basica
from tkinter import messagebox  # caixas de mensagens
from tkinter import ttk  # interface grafica tb

def conectar():
    return sqlite3.connect('teste.db')  # Conecta ao banco de dados 'teste.db'

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        interesse TEXT NOT NULL,
        status TEXT NOT NULL,
        followup TEXT              
        )
    ''')  # Cria a tabela leads com os campos nome, email, telefone, interesse, status e followup
    conn.commit()
    conn.close()

def inserir_lead():
    nome = entry_nome.get()  # Obtém o valor do campo nome
    email = entry_email.get()  # Obtém o valor do campo email
    telefone = entry_telefone.get()  # Obtém o valor do campo telefone
    interesse = combo_interesse.get()  # Obtém o valor do campo interesse
    status = combo_status.get()  # Obtém o valor do campo status
    followup = text_followup.get("1.0", tk.END).strip()  # Obtém o valor do campo followup

    # Verifica se todos os campos foram preenchidos
    if nome and email and telefone and interesse and status:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO leads(nome, email, telefone, interesse, status, followup) VALUES(?,?,?,?,?,?)', 
                  (nome, email, telefone, interesse, status, followup))  # Insere um novo lead no banco de dados
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'LEAD INSERIDO COM SUCESSO!')  # Exibe mensagem de sucesso
        mostrar_leads()
    else:
        messagebox.showerror('ERRO', 'PREENCHA TODOS OS CAMPOS!')  # Exibe mensagem de erro

def mostrar_leads():
    for row in tree.get_children():
        tree.delete(row)  # Remove todos os itens da treeview
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM leads')  # Seleciona todos os leads do banco de dados
    leads = c.fetchall()
    for lead in leads:
        tree.insert("", "end", values=(lead[0], lead[1], lead[2], lead[3], lead[4], lead[5], lead[6]))  # Insere os leads na treeview
    conn.close()

def deletar_lead():
    dado_del = tree.selection()
    if dado_del:
        lead_id = tree.item(dado_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM leads WHERE id = ?', (lead_id,))  # Deleta o lead selecionado
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'LEAD DELETADO')  # Exibe mensagem de sucesso
        mostrar_leads()
    else:
        messagebox.showerror('ERRO', 'SELECIONE UM LEAD PARA DELETAR')  # Exibe mensagem de erro

def editar_lead():
    selecao = tree.selection()
    if selecao:
        lead_id = tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()  # Obtém o novo valor do campo nome
        novo_email = entry_email.get()  # Obtém o novo valor do campo email
        novo_telefone = entry_telefone.get()  # Obtém o novo valor do campo telefone
        novo_interesse = combo_interesse.get()  # Obtém o novo valor do campo interesse
        novo_status = combo_status.get()  # Obtém o novo valor do campo status
        novo_followup = text_followup.get("1.0", tk.END).strip()  # Obtém o novo valor do campo followup

        # Verifica se todos os campos foram preenchidos
        if novo_nome and novo_email and novo_telefone and novo_interesse and novo_status:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE leads SET nome = ?, email = ?, telefone = ?, interesse = ?, status = ?, followup = ? WHERE id = ?', 
                      (novo_nome, novo_email, novo_telefone, novo_interesse, novo_status, novo_followup, lead_id))  # Atualiza o lead no banco de dados
            conn.commit()
            conn.close()
            messagebox.showinfo('AVISO', 'LEAD ATUALIZADO')  # Exibe mensagem de sucesso
            mostrar_leads()
        else:
            messagebox.showwarning('ERRO', 'PREENCHA TODOS OS CAMPOS')  # Exibe mensagem de erro
    else:
        messagebox.showerror('ERRO', 'SELECIONE UM LEAD PARA EDITAR')  # Exibe mensagem de erro

def on_click(event):
    if text_followup.get("1.0", tk.END).strip() == "Exemplo: Entrar em contato novamente em uma semana para discutir a proposta.":
        text_followup.delete("1.0", tk.END)
        text_followup.config(fg='black')

def on_focus_out(event):
    if text_followup.get("1.0", tk.END).strip() == "":
        text_followup.insert(tk.END, "Exemplo: Entrar em contato novamente em uma semana para discutir a proposta.")
        text_followup.config(fg='grey')

janela = tk.Tk()
janela.title('Gerenciamento de Leads')

# Adiciona cor de fundo e ajustes na fonte e tamanho
janela.configure(bg='#f0f0f0')

# Wireframe superior
frame_wireframe = tk.Frame(janela, bg='#d9d9d9')
frame_wireframe.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=10)

# Espaço para o logo
label_logo = tk.Label(frame_wireframe, text='[LOGO]', bg='#d9d9d9', font=('Arial', 20, 'bold'))
label_logo.grid(row=0, column=0, padx=10, pady=10)

# Informações de controle
label_info = tk.Label(frame_wireframe, text='Gerenciador de Leads', bg='#d9d9d9', font=('Arial', 16))
label_info.grid(row=0, column=1, padx=10, pady=10)

# Explicação do gerenciador
label_explicacao = tk.Label(frame_wireframe, text='Este sistema permite gerenciar leads de forma eficiente.', bg='#d9d9d9', font=('Arial', 12))
label_explicacao.grid(row=0, column=2, padx=10, pady=10)

# Frame para os campos de entrada
frame_campos = tk.Frame(janela, bg='#f0f0f0')
frame_campos.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

label_nome = tk.Label(frame_campos, text='Nome*:', bg='#f0f0f0', font=('Arial', 12))
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_nome = tk.Entry(frame_campos, font=('Arial', 12), width=25)
entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky='w')

label_email = tk.Label(frame_campos, text='E-mail*:', bg='#f0f0f0', font=('Arial', 12))
label_email.grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_email = tk.Entry(frame_campos, font=('Arial', 12), width=25)
entry_email.grid(row=1, column=1, padx=5, pady=5, sticky='w')

label_telefone = tk.Label(frame_campos, text='Telefone*:', bg='#f0f0f0', font=('Arial', 12))
label_telefone.grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_telefone = tk.Entry(frame_campos, font=('Arial', 12), width=25)
entry_telefone.grid(row=2, column=1, padx=5, pady=5, sticky='w')

label_interesse = tk.Label(frame_campos, text='Interesse*:', bg='#f0f0f0', font=('Arial', 12))
label_interesse.grid(row=0, column=2, padx=5, pady=5, sticky='e')
combo_interesse = ttk.Combobox(frame_campos, font=('Arial', 12), width=23)
combo_interesse['values'] = ('SEO', 'Marketing de Conteúdo', 'Mídias Sociais', 'Email Marketing', 'Marketing de Influência')  # Valores predefinidos
combo_interesse.grid(row=0, column=3, padx=5, pady=5, sticky='w')

label_status = tk.Label(frame_campos, text='Status*:', bg='#f0f0f0', font=('Arial', 12))
label_status.grid(row=1, column=2, padx=5, pady=5, sticky='e')
combo_status = ttk.Combobox(frame_campos, font=('Arial', 12), width=23)
combo_status['values'] = ('Em andamento', 'Convertido', 'Perdido')  # Valores predefinidos
combo_status.grid(row=1, column=3, padx=5, pady=5, sticky='w')

label_followup = tk.Label(frame_campos, text='Follow-up:', bg='#f0f0f0', font=('Arial', 12))
label_followup.grid(row=2, column=2, padx=5, pady=5, sticky='ne')
text_followup = tk.Text(frame_campos, font=('Arial', 12), width=23, height=5, fg='grey')
text_followup.insert(tk.END, "Exemplo: Entrar em contato novamente em uma semana para discutir a proposta.")
text_followup.grid(row=2, column=3, padx=5, pady=5, sticky='w')
text_followup.bind("<FocusIn>", on_click)
text_followup.bind("<FocusOut>", on_focus_out)

# Informações explicativas
info_text = (
    "→ Preencha todos os campos obrigatórios e selecione os interesses e status apropriados para o lead.\n"
    "→ Use os botões ao lado para salvar, atualizar ou deletar um lead existente."
)
label_info_explicacao = tk.Label(frame_campos, text=info_text, bg='#f0f0f0', font=('Arial', 10), justify='left')
label_info_explicacao.grid(row=3, column=0, columnspan=4, padx=5, pady=10)

# Frame para os botões
frame_botoes = tk.Frame(janela, bg='#f0f0f0')
frame_botoes.grid(row=1, column=1, padx=10, pady=10, sticky='n')

btn_salvar = tk.Button(frame_botoes, text='SALVAR', command=inserir_lead, bg='#4CAF50', fg='white', font=('Arial', 12), width=15)
btn_salvar.grid(row=0, column=0, padx=5, pady=5)

btn_deletar = tk.Button(frame_botoes, text='DELETAR', command=deletar_lead, bg='#F44336', fg='white', font=('Arial', 12), width=15)
btn_deletar.grid(row=1, column=0, padx=5, pady=5)

btn_atualizar = tk.Button(frame_botoes, text='ATUALIZAR', command=editar_lead, bg='#2196F3', fg='white', font=('Arial', 12), width=15)
btn_atualizar.grid(row=2, column=0, padx=5, pady=5)

# Frame para a tabela
frame_tabela = tk.Frame(janela, bg='#f0f0f0')
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Tabela de exibição dos leads
columns = ('ID', 'Nome', 'E-mail', 'Telefone', 'Interesse', 'Status', 'Follow-up')
tree = ttk.Treeview(frame_tabela, columns=columns, show='headings')
tree.pack(expand=True, fill='both')

# Estiliza os cabeçalhos das colunas
style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_leads()

# Ajusta o redimensionamento das colunas
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(2, weight=1)

janela.mainloop()