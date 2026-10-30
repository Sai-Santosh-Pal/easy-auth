document.getElementById('login').addEventListener("submit", async function(event) {
    event.preventDefault()
    alert('clicked')
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
    const url = `https://auth.sai-santosh-pal.hackclub.app/demo/auth/login/${email}/${password}`
    try {
        const response = await fetch(url)
        const data = await response.json()
        console.log(data)
    }
    catch (e) {
        alert(e, 'error')
    }
})