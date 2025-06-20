import os

# --- FUNÇÃO AUXILIAR PARA VALIDAR A ENTRADA DAS NOTAS ---
def get_nota(disciplina):
    """Pede uma nota ao usuário e garante que seja um número válido."""
    while True:
        try:
            # Pede a nota e tenta converter para float
            nota = float(input(f"Digite a nota de {disciplina}: ").replace(',', '.'))
            return nota
        except ValueError:
            # Se o usuário não digitar um número, mostra um erro e pede novamente
            print("❌ Erro: Por favor, digite um número válido para a nota.")

# --- PARTE 1: Coletar dados dos alunos via input ---

print("--- Cadastro de Notas dos Alunos ---")
dados_alunos = []
# O 'range(10)' define que vamos cadastrar 10 alunos
num_alunos = 3

for i in range(num_alunos):
    print(f"\n--- Aluno {i + 1}/{num_alunos} ---")
    
    # Pede o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Pede as notas usando a função auxiliar para garantir que são números
    nota_mat = get_nota("Matemática")
    nota_bio = get_nota("Biologia")
    nota_hist = get_nota("História")
    
    # Adiciona os dados do aluno à lista principal
    dados_alunos.append([nome, nota_mat, nota_bio, nota_hist])

print("\n✅ Cadastro concluído! Gerando arquivos...")

# --- PARTE 2: Criar arquivo de notas, calcular médias e gerar arquivo final ---

arquivo_notas = "notas_alunos.txt"
arquivo_medias = "medias_finais.txt"

try:
    # --- Escreve o arquivo de notas ---
    with open(arquivo_notas, "w", encoding="utf-8") as f:
        for aluno in dados_alunos:
            nome, nota_mat, nota_bio, nota_hist = aluno
            linha = f"{nome},{nota_mat},{nota_bio},{nota_hist}\n"
            f.write(linha)
    
    print(f"✔️ Arquivo '{arquivo_notas}' criado com sucesso!")

    # --- Lê o arquivo de notas, calcula e escreve o arquivo de médias ---
    with open(arquivo_notas, "r", encoding="utf-8") as f_leitura, \
         open(arquivo_medias, "w", encoding="utf-8") as f_escrita:
        
        for linha in f_leitura:
            partes = linha.strip().split(',')
            
            nome_aluno = partes[0]
            nota1 = float(partes[1])
            nota2 = float(partes[2])
            nota3 = float(partes[3])
            
            media = (nota1 + nota2 + nota3) / 3
            
            linha_media = f"{nome_aluno}: {media:.2f}\n"
            f_escrita.write(linha_media)

    print(f"✔️ Arquivo '{arquivo_medias}' com as médias foi gerado com sucesso!")
    
    # Mostra o caminho completo dos arquivos gerados
    print("\n📍 Arquivos salvos em:")
    print(os.path.abspath(arquivo_medias))

except Exception as e:
    print(f"🚨 Ocorreu um erro inesperado durante a criação dos arquivos: {e}")