// auth.js

const TOKEN_KEY = 'token';

// Guardar el token en localStorage
export const saveToken = (token) => {
  localStorage.setItem(TOKEN_KEY, token);
};

// Obtener el token desde localStorage
export const getToken = () => {
  return localStorage.getItem(TOKEN_KEY);
};

// Eliminar el token de localStorage
export const removeToken = () => {
  localStorage.removeItem(TOKEN_KEY);
};
