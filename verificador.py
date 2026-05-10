# Verificador de Preços
import json

class VerificadorPrecos:
    def __init__(self):
        self.produtos = {}  # {nome: {'preço': float, 'histórico': []}}
    
    def adicionar_produto(self, nome, preco):
        """Adiciona um novo produto com preço inicial."""
        if nome in self.produtos:
            print(f"❌ Produto '{nome}' já existe!")
            return
        self.produtos[nome] = {
            'preço': preco,
            'histórico': [preco]
        }
        print(f"✅ Produto '{nome}' adicionado com preço R${preco:.2f}")
    
    def atualizar_preco(self, nome, novo_preco):
        """Atualiza o preço de um produto."""
        if nome not in self.produtos:
            print(f"❌ Produto '{nome}' não encontrado!")
            return
        
        preco_antigo = self.produtos[nome]['preço']
        self.produtos[nome]['preço'] = novo_preco
        self.produtos[nome]['histórico'].append(novo_preco)
        
        diferenca = novo_preco - preco_antigo
        if diferenca > 0:
            print(f"📈 '{nome}': R${preco_antigo:.2f} → R${novo_preco:.2f} (↑ R${diferenca:.2f})")
        elif diferenca < 0:
            print(f"📉 '{nome}': R${preco_antigo:.2f} → R${novo_preco:.2f} (↓ R${abs(diferenca):.2f})")
        else:
            print(f"➡️ '{nome}': Preço sem alteração (R${novo_preco:.2f})")
    
    def listar_produtos(self):
        """Lista todos os produtos e seus preços."""
        if not self.produtos:
            print("❌ Nenhum produto cadastrado!")
            return
        
        print("\n📋 LISTA DE PRODUTOS:")
        print("-" * 50)
        for nome, dados in self.produtos.items():
            print(f"{nome:.<30} R${dados['preço']:>8.2f}")
        print("-" * 50)
    
    def produto_mais_barato(self):
        """Retorna o produto com o menor preço."""
        if not self.produtos:
            print("❌ Nenhum produto cadastrado!")
            return
        
        mais_barato = min(self.produtos.items(), key=lambda x: x[1]['preço'])
        print(f"💰 Produto mais barato: '{mais_barato[0]}' - R${mais_barato[1]['preço']:.2f}")
    
    def produto_mais_caro(self):
        """Retorna o produto com o maior preço."""
        if not self.produtos:
            print("❌ Nenhum produto cadastrado!")
            return
        
        mais_caro = max(self.produtos.items(), key=lambda x: x[1]['preço'])
        print(f"💎 Produto mais caro: '{mais_caro[0]}' - R${mais_caro[1]['preço']:.2f}")
    
    def calcular_total(self):
        """Calcula o valor total de todos os produtos."""
        if not self.produtos:
            print("❌ Nenhum produto cadastrado!")
            return
        
        total = sum(dados['preço'] for dados in self.produtos.values())
        print(f"💵 Valor total: R${total:.2f}")
        return total
    
    def historico_preco(self, nome):
        """Mostra o histórico de preços de um produto."""
        if nome not in self.produtos:
            print(f"❌ Produto '{nome}' não encontrado!")
            return
        
        historico = self.produtos[nome]['histórico']
        print(f"\n📊 Histórico de '{nome}':")
        for i, preco in enumerate(historico, 1):
            print(f"  {i}. R${preco:.2f}")
        
        if len(historico) > 1:
            variacao = historico[-1] - historico[0]
            print(f"  Variação total: R${variacao:.2f}")
    
    def filtrar_por_faixa_preco(self, preco_min, preco_max):
        """Filtra e lista produtos dentro de uma faixa de preço."""
        if not self.produtos:
            print("❌ Nenhum produto cadastrado!")
            return
        
        produtos_filtrados = {
            nome: dados for nome, dados in self.produtos.items()
            if preco_min <= dados['preço'] <= preco_max
        }
        
        if not produtos_filtrados:
            print(f"❌ Nenhum produto encontrado na faixa R${preco_min:.2f} - R${preco_max:.2f}")
            return
        
        print(f"\n🔍 PRODUTOS NA FAIXA R${preco_min:.2f} - R${preco_max:.2f}:")
        print("-" * 50)
        for nome, dados in produtos_filtrados.items():
            print(f"{nome:.<30} R${dados['preço']:>8.2f}")
        print("-" * 50)
        print(f"Total de produtos encontrados: {len(produtos_filtrados)}")
    
    def adicionar_produtos_interativo(self):
        """Permite adicionar produtos interativamente via input do usuário."""
        print("\n🛒 ADICIONAR PRODUTOS INTERATIVAMENTE")
        print("Digite 'sair' no nome do produto para parar.")
        
        while True:
            nome = input("Nome do produto: ").strip()
            if nome.lower() == 'sair':
                break
            
            try:
                preco = float(input("Preço do produto: ").strip())
                if preco < 0:
                    print("❌ Preço não pode ser negativo!")
                    continue
                self.adicionar_produto(nome, preco)
            except ValueError:
                print("❌ Preço inválido! Digite um número válido.")
    
    def salvar_dados(self, arquivo="produtos.json"):
        """Salva os produtos em um arquivo JSON."""
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(self.produtos, f, indent=4, ensure_ascii=False)
            print(f"✅ Dados salvos em '{arquivo}'")
        except Exception as e:
            print(f"❌ Erro ao salvar dados: {e}")
    
    def remover_produto(self, nome):
        """Remove um produto da lista."""
        if nome not in self.produtos:
            print(f"❌ Produto '{nome}' não encontrado!")
            return False
        
        del self.produtos[nome]
        print(f"🗑️ Produto '{nome}' removido com sucesso!")
        return True
    
    def carregar_dados(self, arquivo="produtos.json"):
        """Carrega os produtos de um arquivo JSON."""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                self.produtos = json.load(f)
            print(f"✅ Dados carregados de '{arquivo}' ({len(self.produtos)} produtos)")
        except FileNotFoundError:
            print(f"❌ Arquivo '{arquivo}' não encontrado!")
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")


# ===== EXEMPLO DE USO =====
if __name__ == "__main__":
    verificador = VerificadorPrecos()
    
    # Tentar carregar dados salvos
    verificador.carregar_dados()
    
    # Adicionar produtos (modo interativo ou hardcoded)
    print("Escolha o modo de adição de produtos:")
    print("1. Adicionar produtos interativamente")
    print("2. Usar produtos de exemplo")
    escolha = input("Digite 1 ou 2: ").strip()
    
    if escolha == "1":
        verificador.adicionar_produtos_interativo()
    else:
        # Adicionar produtos de exemplo
        verificador.adicionar_produto("Notebook", 3500.00)
        verificador.adicionar_produto("Mouse", 150.00)
        verificador.adicionar_produto("Teclado", 450.00)
        verificador.adicionar_produto("Monitor", 1200.00)
    
    # Listar produtos
    verificador.listar_produtos()
    
    # Atualizar preços
    print("\n🔄 Atualizando preços...")
    verificador.atualizar_preco("Notebook", 3200.00)
    verificador.atualizar_preco("Mouse", 180.00)
    
    # Informações
    print()
    verificador.produto_mais_barato()
    verificador.produto_mais_caro()
    verificador.calcular_total()
    
    # Histórico
    verificador.historico_preco("Notebook")
    
    # Filtrar por faixa de preço
    print("\n🔍 Testando filtros...")
    verificador.filtrar_por_faixa_preco(100, 500)  # Produtos entre R$100 e R$500
    verificador.filtrar_por_faixa_preco(1000, 4000)  # Produtos entre R$1000 e R$4000
    
    # Salvar dados
    verificador.salvar_dados()
