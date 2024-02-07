
import "./signUp.css";

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signUp } from '../../services/service'; 
import {Link} from "react-router-dom";

function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [image, setImage] = useState(null); // Estado para almacenar la imagen seleccionada
    const [error, setError] = useState("");

    const handleSignUp = async (e) => {
        e.preventDefault();
        try {
            let imageData = null;
            if (image) {
                // Si se selecciona una imagen, conviértela a formato base64
                const reader = new FileReader();
                reader.onload = async () => {
                    imageData = reader.result;
                    const data = await signUp(username, password, imageData);
                    if (!data.detail) {
                        navigate(`/`);
                    } else {
                        setError(data.detail);
                    }
                };
                reader.readAsDataURL(image);
            } else {
                // Si no se selecciona ninguna imagen, usa la imagen por defecto
                const defaultImage = "https://w7.pngwing.com/pngs/81/570/png-transparent-profile-logo-computer-icons-user-user-blue-heroes-logo.png";
                const data = await signUp(username, password, imageData);
                    if (!data.detail) {
                        navigate(`/`);
                    } else {
                        setError(data.detail);
                    }
            }
        } catch (error) {
            setError('Error al crear la cuenta');
        }
    };

    return (
        <div className="login">
            <h1>Sign Up</h1>
            <form method="post" onSubmit={handleSignUp}>
                {error && <div className="error">{error} <br /></div>}
                <input type="text" name="user" placeholder="Usuario" required onChange={(e) => setUsername(e.target.value)} />
                <input type="password" name="password" placeholder="Contraseña" onChange={(e) => setPassword(e.target.value)} required />
                <input type="file" accept="image/*" onChange={(e) => setImage(e.target.files[0])} /> {/* Campo para seleccionar una imagen */}
                <button type="submit" className="btn btn-primary btn-block btn-large">Crear cuenta</button>
            </form>
            <Link to="/"> Iniciar sesión </Link>
        </div>
    );
}
export default Login;