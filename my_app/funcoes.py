
#organização variáveis
var_quant = [
    "idade", 
    "horascontratuais", 
    "salario", 
    "valorsalariofixo"]

var_quali = [
    "nome_ocu",
    "grau",
    "racacor",
    "sexo",
    "tipodedeficiencia",
    "tipomovimentacao"]

label_quali = {
  "sexo": {
      1: 'Homem', 
      3: 'Mulher', 
      9: 'Não Identificado'},
  "racacor":{
      1: 'Branca', 
      2: 'Preta', 
      3: 'Parda', 
      4: 'Amarela', 
      5: 'Indígena', 
      6: 'Não informada', 
      9: 'Não Identificado'},
  "grau": {
      1: "Analfabeto",
      2: "Até 5ª Incompleto",
      3: "5ª Completo Fundamental",
      4: "6ª a 9ª Fundamental",
      5: "Fundamental Completo",
      6: "Médio Incompleto",
      7: "Médio Completo",
      8: "Superior Incompleto",
      9: "Superior Completo",
      10: "Mestrado",
      11: "Doutorado",
      80: "Pós-Graduação completa",
      99: "Não Identificado"},
  "tipodedeficiencia": {
      0:"Não Deficiente",
      1:"Física",
      2:"Auditiva",
      3:"Visual",
      4:"Intelectual (Mental)",
      5:"Múltipla",
      6:"Reabilitado",
      9:"Não Identificado"
}}

# Função para construir gráfico de barras
def grafico_barras_prop(data, variable):
    (data[[variable]]
     .value_counts(normalize=True, sort = False)
     .rename("Proportion")
     .reset_index()
     .pipe((sns.barplot, "data"), x=variable, y="Proportion"))
    plt.ylim(0,1)
    plt.show()

# Função para construir gráfico de distribuição
def generate_plot(df, row, col):
    plt.figure(figsize=(25,40));
    for i, feat in enumerate(df):
        plt.subplot(row,col, i+1)
        if df[feat].dtypes == 'object':
            sns.countplot(y=df[feat])
            #plt.xticks(rotation=90)
            plt.tight_layout();
        else:
            sns.distplot(x=df[feat], color='c')
            plt.tight_layout();
            plt.xlabel(feat);