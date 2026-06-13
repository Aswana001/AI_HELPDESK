async function login() {

    const identifier =
        document.getElementById(
            "identifier"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;

    if (!identifier || !password) {
        alert("Please fill in all fields");
        return;
    }

    try {
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

        console.log("Response Status:", response.status);
        console.log("Response Data:", data);

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

        } else {
            // Show actual error from server
            const errorMsg = data.non_field_errors?.[0] || 
                           data.identifier?.[0] || 
                           data.password?.[0] ||
                           JSON.stringify(data);
            
            alert(
                "Login Failed: " + errorMsg
            );
        }

    } catch (error) {
        alert("Error: " + error.message);
        console.error(error);
    }
}