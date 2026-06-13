async function login() {

    const identifier =
        document.getElementById(
            "identifier"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;

    const response =
        await fetch(
            "/api/accounts/login/",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({
                    identifier,
                    password
                })
            }
        );

    const data =
        await response.json();

    console.log(data);

    if(response.ok){

        localStorage.setItem(
            "access",
            data.access
        );

        localStorage.setItem(
            "role",
            data.user.role
        );

        if(data.user.role === "admin"){

            window.location.href =
                "/admin-dashboard/";

        }else{

            window.location.href =
                "/dashboard/";
        }

    }else{

        alert(
            "Login Failed"
        );
    }
}