// Importing modules
import React, { useRef, useState } from "react";
import Greyscale from "./Greyscale";
import Home from "./Home";
// import "./Sidebar.css";

function Sidebar() {
  const [feature, setFeature] = useState(<Home />);

  function changeFeature(event) {
    if (event.target.getAttribute("value") === "greyscale")
      setFeature(<Greyscale />);
    // else if(event.target.value === "rotate") setFeature(<Rotate />);
  }

  return (
    <div class="sidenav">
      <a href="#" value="greyscale" onClick={changeFeature}>
        Greyscale
      </a>
      <a href="#">basic feature</a>
      <a href="#">basic feature</a>
      <a href="#">basic feature</a>
      <a href="#">advanced feature</a>
      <a href="#">advanced feature</a>
      <a href="#">advanced feature</a>
      <a href="#">advanced feature</a>
    </div>
  );
}

export default Sidebar;
