window.onload = function () {
    fetch('/api/health')
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerText =
            "Status: " + data.status +
            " | Host: " + data.hostname +
            " | DB: " + data.database;
    })
    .catch(error => {
        document.getElementById('status').innerText =
            "Backend not reachable ❌";
    });
};
