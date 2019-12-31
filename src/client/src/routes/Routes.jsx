import React from "react";
import { Route, Switch } from "react-router-dom";
import DashboardRoutes from "./DashboardRoutes";
import Login from "./Login";
import Register from "./Register";
import About from "./About";
import Contact from "./Contact";
import Home from "./Home";
import NavBarPublic from "./NavbarPublic";
import NoMatch from "./NoMatch";

const Routes = () => {
  return (
    <>
      <Route path="/" component={NavBarPublic} />
      <Switch>
        <Route path="/" exact render={() => <Home />} />
        <Route path="/dash" render={() => <DashboardRoutes />} />
        <Route path="/login" render={() => <Login />} />
        <Route path="/register" render={() => <Register />} />
        <Route path="/about" render={() => <About />} />
        <Route path="/contact" render={() => <Contact />} />
        <Route component={NoMatch} />
      </Switch>
    </>
  );
};

export default Routes;
