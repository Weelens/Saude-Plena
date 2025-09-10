from flask import Flask, render_template,request,redirect,blueprints
import os
from dotenv import load_dotenv
import openai

routes = blueprints('routes', __name__)
load_dotenv()
openai.api_key= os.getenv("OPENAI_API_KEY")

@routes.route('/gerar_treino', methods=['GET','POST'])
def gerar_treino():
    if request.method == 'POST':
        idade = request.form['idade']
        peso = request.form['peso']
        sexo = request.form['sexo']
        objetivo = request.form['objetivo']

        prompt = f"""
        Crie uma rotina de treino semanal personalizada para uma pessoa do sexo {sexo}, com {idade} anos e {peso}kg, com o objetivo de {objetivo}.
        """