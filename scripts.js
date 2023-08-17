function generateUUIDFromCredentials(username, password) {
    async function sha256(message) {
        const encoder = new TextEncoder();
        const data = encoder.encode(message);

        const buffer = await crypto.subtle.digest('SHA-256', data);
        const hexDigest = Array.from(new Uint8Array(buffer))
            .map(byte => byte.toString(16).padStart(2, '0'))
            .join('');

        return hexDigest;
    }

    return sha256(username + password);
}

function removeURLParameters() {
    const [baseURL, params] = window.location.href.split('?');
    window.location.href = baseURL;
}

window.onload = async () => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    if (urlParams.has("usr") && urlParams.has("pwd")) {
        const username = urlParams.get("usr");
        const password = urlParams.get("pwd");

        let UUID = await generateUUIDFromCredentials(username, password);
        console.debug(UUID);
        localStorage.setItem("UUID", UUID)
        localStorage.setItem("username", username)
        removeURLParameters()
    }
    if (!localStorage.getItem("UUID")) {
        window.location.href = "/login"
    }
    const UUID = localStorage.getItem("UUID")
    console.debug(UUID)
} 
