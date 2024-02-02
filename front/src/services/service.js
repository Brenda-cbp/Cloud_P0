import React from 'react';

const back ="http://127.0.0.1:8000"
const login = async (username, password) => {
    try {
        const response = await fetch(back+'/usuarios/iniciar-sesion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre_usuario: username,
                contrasenia: password
            })
        });
        console.log(response)
        if (!response.ok) {
            throw new Error('Error al iniciar sesión');
        }

        const data = await response.json();
        return data; // Retorna los datos del usuario si la solicitud fue exitosa
    } catch (error) {
        throw new Error('Error al iniciar sesión:', error);
    }
};

const signUp = async (username, password, image) => {
    try {
        const response = await fetch(back+'/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre_usuario: username,
                contrasenia: password,
                imagen_perfil: image
            })
        });

        const data = await response.json();
        return data; // Retorna los datos del usuario si la solicitud fue exitosa
    } catch (error) {
        throw new Error('Error al iniciar sesión:', error);
    }
};
export { login, signUp };
