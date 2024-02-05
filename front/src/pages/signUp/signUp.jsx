
import "./signUp.css";

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signUp } from '../../services/service'; 
import {Link} from "react-router-dom";

function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSingUp = async (e) => {
        e.preventDefault();
        console.log(e)
        try {
            const data = await signUp(username, password, "imagen");
            console.log(data)
            if (!data.detail) {
                navigate(`/`);
            } else {
                setError(data.detail);
            }
        } catch (error) {
            setError('Error al iniciar sesión');
        }
    };

    return (
        <div className="login">
            <h1>Sign Up</h1>
            <form method="post" onSubmit={handleSingUp}>
                {error && <div className="error">{error}  <br /> </div> } 
                <input type="" name="user" placeholder="Usuario" required onChange={(e) => setUsername(e.target.value)} />
                <input type="password" name="password" placeholder="Contraseña" onChange={(e) => setPassword(e.target.value)} required />
                <button type="submit" className="btn btn-primary btn-block btn-large">Crear cuenta</button>
            </form>
            <Link to="/"> Iniciar sesión </Link>

        </div>
    );
}

export default Login;
