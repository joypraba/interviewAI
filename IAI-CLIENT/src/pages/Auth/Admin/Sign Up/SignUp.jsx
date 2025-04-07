import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { recruiterSignUp, candidateSignUp } from "../../../../services/Auth";

const SignUp = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const locparams = new URLSearchParams(location.search);
  const role = locparams.get("role");

  const [params, setParams] = useState({ name: "", email: "", password: "" });

  const handleChange = (e) => {
    setParams({
      ...params,
      [e.target.name]: e.target.value,
    });
  };

  const login = () => {
    if (role == 1) {
      navigate("/admin?role=1");
    } else if (role == 2) {
      navigate("/candidate?role=2");
    } else {
      navigate("/");
    }
  };

  const signUpService = async () => {
    try {
      if (role == 1) {
        const response = await recruiterSignUp(params);
        if (response) navigate("/admin?role=1");
      } else if (role == 2) {
        const formData = new FormData();
        formData.append("name", params.name);
        formData.append("email", params.email);
        formData.append("password", params.password);
        console.log(params)
        const response = await candidateSignUp(params);
        if (response) navigate("/candidate?role=2");
      } else {
        navigate("/");
      }
    } catch (e) {
      console.log(e.message);
    }
  };

  return (
    <main className="d-flex w-100">
      <div className="container d-flex flex-column">
        <div className="row vh-100">
          <div className="col-sm-10 col-md-8 col-lg-6 col-xl-5 mx-auto d-table h-100">
            <div className="d-table-cell align-middle">
              <div className="text-center mt-4">
                <h1 className="h2">Get started</h1>
                <p className="lead">
                  Start creating the best possible user experience for your customers.
                </p>
              </div>

              <div className="card">
                <div className="card-body">
                  <div className="m-sm-3">
                    <form>
                      <div className="mb-3">
                        <label className="form-label">Full name</label>
                        <input
                          className="form-control form-control-lg"
                          type="text"
                          name="name"
                          placeholder="Enter your name"
                          onChange={handleChange}
                          value={params.name}
                        />
                      </div>
                      <div className="mb-3">
                        <label className="form-label">Email</label>
                        <input
                          className="form-control form-control-lg"
                          type="email"
                          name="email"
                          placeholder="Enter your email"
                          onChange={handleChange}
                          value={params.email}
                        />
                      </div>
                      <div className="mb-3">
                        <label className="form-label">Password</label>
                        <input
                          className="form-control form-control-lg"
                          type="password"
                          name="password"
                          placeholder="Enter password"
                          onChange={handleChange}
                          value={params.password}
                        />
                      </div>
                      <div className="d-grid gap-2 mt-3">
                        <button
                          type="button"
                          className="btn btn-lg btn-primary"
                          onClick={signUpService}
                        >
                          Sign up
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>

              <div className="text-center mb-3">
                Already have an account? <a onClick={login}>Log In</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default SignUp;
