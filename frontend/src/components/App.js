// Importing modules
import React, { useRef, useState } from "react";
import "../App.css";
import Home from "./Home";
import Greyscale from "./Greyscale";
import Rotate from "./Rotate";
import Crop from "./Crop";
import Cartoon from "./Cartoon";
import Denoise from "./Denoise";
import Edge from "./Edge";
import Otsu from "./Otsu";
import Canny from "./Canny";
import Blur from "./Blur";
import AddText from "./AddText";
import AddSub from "./AddSub";
import DogFilter from "./DogFilter";
import HatSpecFilter from "./HatSpecFilter";

function App() {
  const [feature, setFeature] = useState(<Home />);
  function changeFeature(event) {
    if (event.target.getAttribute("value") === "greyscale")
      setFeature(<Greyscale />);
    else if (event.target.getAttribute("value") === "rotate")
      setFeature(<Rotate />);
    else if (event.target.getAttribute("value") === "crop")
      setFeature(<Crop />);
    else if (event.target.getAttribute("value") === "cartoon")
      setFeature(<Cartoon />);
    else if (event.target.getAttribute("value") === "denoise")
      setFeature(<Denoise />);
    else if (event.target.getAttribute("value") === "edge")
      setFeature(<Edge />);
    else if (event.target.getAttribute("value") === "otsu")
      setFeature(<Otsu />);
    else if (event.target.getAttribute("value") === "canny")
      setFeature(<Canny />);
    else if (event.target.getAttribute("value") === "blur")
      setFeature(<Blur />);
    else if (event.target.getAttribute("value") === "text")
      setFeature(<AddText />);
    else if (event.target.getAttribute("value") === "addsub")
      setFeature(<AddSub />);
    else if (event.target.getAttribute("value") === "dogFilter")
      setFeature(<DogFilter />);
    else if (event.target.getAttribute("value") === "hatSpec")
      setFeature(<HatSpecFilter />);
  }

  return (
    <div className="main-div">
      <div className="feature-div">{feature}</div>
      <div className="sidenav">
        <a href="#" value="greyscale" onClick={changeFeature}>
          Greyscale
        </a>
        <a href="#" value="rotate" onClick={changeFeature}>
          Rotate
        </a>
        {/* <a href="#" value="crop" onClick={changeFeature}>
          Crop
        </a> */}
        <a href="#" value="cartoon" onClick={changeFeature}>
          Cartoon
        </a>
        <a href="#" value="denoise" onClick={changeFeature}>
          Denoise
        </a>
        <a href="#" value="edge" onClick={changeFeature}>
          Edge Detection
        </a>
        <a href="#" value="otsu" onClick={changeFeature}>
          Otsu's Thresholding
        </a>
        <a href="#" value="canny" onClick={changeFeature}>
          Canny Filter
        </a>
        <a href="#" value="blur" onClick={changeFeature}>
          Blur Filter
        </a>
        <a href="#" value="text" onClick={changeFeature}>
          Add Text
        </a>
        <a href="#" value="addsub" onClick={changeFeature}>
          Add or Subtract Images
        </a>
        <a href="#" value="dogFilter" onClick={changeFeature}>
          Dog Filter
        </a>
        <a href="#" value="hatSpec" onClick={changeFeature}>
          Hat and Specs
        </a>
      </div>
    </div>
  );
}

export default App;
