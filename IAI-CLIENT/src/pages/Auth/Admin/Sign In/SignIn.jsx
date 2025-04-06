import React, {useState} from "react";
import "./SignIn.css"
import { Link, useLocation  } from "react-router-dom";
// import { Button } from "bootstrap";
import { logIn } from "../../../../services/Auth";
const Login = () => {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const role = params.get("role");

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const signIn = async () => {
    try {
      const data = {
        email,
        password,
        type: role
      }
      console.log(data)
      const response = await logIn(data)
      console.log(response)
    } catch (e) {
      console.log(e.message)
    }
  }

  console.log("User Role:", role);
  return (
    
    <main className="d-flex w-100">
      <div className="container d-flex flex-column">
        <div className="row vh-100">
          <div className="col-sm-10 col-md-8 col-lg-6 col-xl-5 mx-auto d-table h-100">
            <div className="d-table-cell align-middle">

              <div className="text-center mt-4">
                <h1 className="h2">Welcome back!</h1>
                <p className="lead">Sign in to your account to continue</p>
              </div>

              <div className="card">
                <div className="card-body">
                  <div className="m-sm-3">
                      <div className="mb-3">
                        <label className="form-label">Email</label>
                        <input
                          className="form-control form-control-lg"
                          type="email"
                          name="email"
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="Enter your email"
                        />
                      </div>
                      <div className="mb-3">
                        <label className="form-label">Password</label>
                        <input
                          className="form-control form-control-lg"
                          type="password"
                          name="password"
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="Enter your password"
                        />
                      </div>
                      <div>
                        <div className="form-check align-items-center">
                          <input
                            id="customControlInline"
                            type="checkbox"
                            className="form-check-input"
                            value="remember-me"
                            name="remember-me"
                            defaultChecked
                          />
                          <label
                            className="form-check-label text-small"
                            htmlFor="customControlInline"
                          >
                            Remember me
                          </label>
                        </div>
                      </div>
                      <div className="d-grid gap-2 mt-3">
                        <button className="btn btn-lg btn-primary" onClick={signIn}>
                          Sign in
                        </button>
                        {/* <Link to="/admin/dashboard">Sign In</Link> */}
                      </div>
                  </div>
                </div>
              </div>

              <div className="text-center mb-3">
                Don't have an account?{" "}
                <Link to="/admin/sign-up">Sign up</Link>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Login;
