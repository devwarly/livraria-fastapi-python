function btnCadastrar(){
    const formCard = document.getElementById("card-form");
    const blur = document.getElementById("blur");

    if (formCard.style.display == "none"){
        formCard.style.display = "flex";
        blur.style.display = "flex";
    }else{
        formCard.style.display = "none";
        blur.style.display = "none";
    }
}

const API_URL = "http://localhost:8030/livros";

const listaLivros = document.getElementById("livrosList");
const formLivro = document.getElementById("formLivro");

// Adicionar Livros
formLivro.addEventListener("submit", async (event) => {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const ano_publicacao = Number(document.getElementById("ano_publicacao").value);

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(
            {
                titulo: titulo,
                autor: autor,
                ano_publicacao: ano_publicacao
            }
        )
    });
    formLivro.reset();
});