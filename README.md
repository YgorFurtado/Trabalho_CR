

Este projeto visa analisar redes de transportes urbanos, criando grafos a partir de dados de linhas de ônibus municipais de São Bernardo do Campo e manipulando essas estruturas para analizar as conexões entre os bairros.
## Descrição dos Arquivos

### Código

- **CriaLista_1.py**: Gera uma lista que pode ser importada pelo Gephi, onde é criado um vértice entre bairros que são seguidos um do outro em cada linha de ônibus.
- **CriaLista_2.py**: Gera uma lista para importação pelo Gephi, criando vértices entre todos os bairros de uma determinada linha de ônibus.
- **CriaMatriz.py**: Converte uma lista no formato do Gephi para uma matriz de adjacência.
- **LerMatriz.py**: Lê uma matriz de adjacência de um grafo e retorna informações sobre ele.
- **ygorfuncoes.py**: Contém funções auxiliares utilizadas nos scripts acima.

### Dados

- **database**: Contém arquivos de dados e documentos de suporte utilizados para a análise e geração dos grafos.

### Workspace

- **workspace**: Diretório onde são armazenados os projetos do Gephi e as exportações dos grafos gerados, em diversos formatos.

## Licença

Este projeto é licenciado sob os termos da licença MIT.
