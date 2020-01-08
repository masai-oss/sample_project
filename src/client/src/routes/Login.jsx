import React from "react";
import { Link } from "react-router-dom";

const Login = () => {
  return (
    <>
      <div>LOGIN PAGE</div>
      <form>
        <div>
          <input type="email" placeholder="Email" />
        </div>
        <div>
          <input type="password" placeholder="Password" />
        </div>
        <div>
          <input type="submit" value="Log in" />
        </div>
      </form>
      <Link to="/dash">GOTO DASHBOARD</Link>
    </>
  );
};

export default Login;
