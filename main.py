import requests
import streamlit as st

URL = "https://api.github.com"

def selecionarUsuario(usuario):
    url = f'{URL}/users/{usuario}'
    response = requests.get(url)
    if(response.status_code == 200):
        return response.json()
    else:
        return None


def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Consulta Github')
    username = st.text_input('Insira o username de usuario github')

    if(st.button('buscar')):
        infoUsuario = selecionarUsuario(username)
        if(infoUsuario is not None):
            st.markdown(f'''                        
                <div class="card" style="width: 18rem; justify-content: center;">
                    <img class="card-img-top" src="{infoUsuario['avatar_url']}" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{infoUsuario['name']}</h5>
                        <p class="card-text">{infoUsuario['bio']}</p>
                        <a href="{infoUsuario['html_url']}" class="btn btn-success" style='color:#fff;'>Acesse o GitHub</a>
                    </div>
                </div> ''', unsafe_allow_html=True)


ui()
