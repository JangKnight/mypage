import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";
import { bdays } from "./bdays";
import Bday from "./Bday";
const BdayList = () => {
  return (
    <section>
      {bdays.map((bday) => {
        return <Bday {...bday} key={bday.id} />;
      })}
    </section>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<BdayList />);
