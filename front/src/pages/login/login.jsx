
import "./login.css";

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login } from '../../services/service'; // Importa la función de inicio de sesión

function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await login(username, password);
            if (data) {
                navigate(`/${username}/tareas`);
            } else {
                setError('Invalid username or password');
            }
        } catch (error) {
            setError('Error al iniciar sesión');
        }
    };

    return (
        <div className="login">
            <h1>Login</h1>
            <form method="post" onSubmit={handleLogin}>
                {error && <div className="error">{error}</div>}
                <input type="" name="user" placeholder="Usuario" required onChange={(e) => setUsername(e.target.value)} />
                <input type="password" name="password" placeholder="Contraseña" onChange={(e) => setPassword(e.target.value)} required />
                <button type="submit" className="btn btn-primary btn-block btn-large">
                    Ingresar</button>
            </form>
        </div>
    );
}

export default Login;
