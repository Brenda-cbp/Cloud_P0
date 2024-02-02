import { Route, Routes } from "react-router-dom";
import React from 'react';
import Home from "../pages/home/home";
import Login from "../pages/login/login";
import SignUp from "../pages/signUp/signUp";
import Recomendation from "../pages/recomendation/recomendation";

const CreateRoutes = () => (
    <Routes>
        <Route exact path="/" element={<Login />} />
        <Route exact path="/SignUp" element={<SignUp />} />
        <Route exact path="/:id/tareas" element={<Home />} />
        <Route exact path="/:id/:idPelicula/recomendaciones" element={<Recomendation />} />
    </Routes>
);

export default CreateRoutes;