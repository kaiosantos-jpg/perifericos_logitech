# import streamlit as st

# ##aqui eu coloco o titulo
# st.title('Olá, devs!')

# ##digitando algo
#st.write('Eu adoro fazer programação em python com o professor Mateus!')

# #criando um calendario
# date = st.date_input("selecione uma data")

# ##permitindo o upload do aqruivo
# file = st.file_uploader("Pick a File")



#python -m streamlit run app.py
#write = escrever algo
#title = titulo
#date = inserir data
#file = inserir um arqvuivo

import streamlit as st
import pandas as pd

#sidebar

st.sidebar.image("logo_logitech.png")
st.sidebar.title('Peripherals For You')

produtos = ['Teclado PRO X 60', 'Teclado G915 TKL', 'Teclado PRO X TKL', 'Teclado G715', 'Teclado G815', 'Teclado PRO', 'Mouse G305', 'Mouse PRO X SUPERLIGHT', 'Mouse G703', 'Mouse G203', 'Mouse G502 X LIGHTSPEED' , 'Mouse G403 HERO', 'Logitech MOUSE PAD - Studio Series', 'MousePad G740', 'MousePad G440']

opcao = st.sidebar.selectbox('Escolha o produto que deseja comprar', produtos)

#Principal
st.title('Logitech Store')

st.image(f'{opcao}.png')
st.markdown(f'## Você está prestes a comprar o: {opcao}')
st.markdown('---')


quantidade_comprada = st.text_input(f'Quantos produtos você deseja comprar?')



###COpia aqui agora

if opcao == 'Teclado PRO X 60':
    valor =1169.91
    
elif opcao == 'Teclado G915 TKL':
    valor =  1299.90

elif opcao == 'Teclado PRO X TKL':
    valor = 1439.91
    
elif opcao == 'Teclado G715':
    valor = 1259.91
    
elif opcao == 'Teclado G815':
    valor = 830
    
elif opcao == 'Teclado PRO':
    valor = 656.91
    
elif opcao == 'Mouse G305':
    valor = 332.91
    
elif opcao == 'Mouse PRO X SUPERLIGHT':
    valor =  799.90
 
elif opcao == 'Mouse G703':
    valor = 569.90
    
elif opcao == 'Mouse G203':
    valor = 189.90
    
elif opcao == 'Mouse G502 X LIGHTSPEED':
    valor = 799.90
    
elif opcao == 'Mouse G403 HERO':
    valor = 299.90

elif opcao == 'Logitech MOUSE PAD - Studio Series':
    valor = 44.91
    
elif opcao == 'MousePad G740':
    valor = 290.31
    
elif opcao == 'MousePad G440':
    valor = 193.76
    
    
    
    
if st.button('calcular'):
    quantidade_comprada = int(quantidade_comprada)
    valor_total = quantidade_comprada * valor
    
 
    
    st.warning(f'Você comprou {quantidade_comprada} produtos {opcao} por :{valor_total:.2f}')
