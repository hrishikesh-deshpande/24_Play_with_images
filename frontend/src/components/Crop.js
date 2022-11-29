// Importing modules
import React, { useRef, useState } from "react";
import { saveAs } from "file-saver";
import { Helmet } from "react-helmet";

function Crop() {
  const form = useRef(null);
  const [file, setFile] = useState();

  const submit = (e) => {
    e.preventDefault();
    const primary_image = document.querySelector("#primary_image");
    const data =
      primary_image.files.length == 0 ? [] : new FormData(form.current);
    fetch("/greyscale", {
      method: "POST",
      body: data,
      encType: "multipart/form-data",
    })
      .then((res) => res.json())
      .then((json) => {
        const outimg = document.getElementById("outimg");
        if (json.status == 200)
          outimg.src = `data:image/jpg;base64, ${json.processed_image}`;
        else console.log(json.message);
      });
  };

  const download = () => {
    const outimgsrc = document.getElementById("outimg").getAttribute("src");
    if (outimgsrc) saveAs(outimgsrc, "imagical.jpg");
    else alert("No output generated");
  };

  function preview(e) {
    setFile(URL.createObjectURL(e.target.files[0]));
  }

  return (
    <div>
      <h3>Upload an image to crop</h3>
      <form ref={form} onSubmit={submit}>
        <input
          id="primary_image"
          type="file"
          accept="image/*"
          name="photo"
          onChange={preview}
        />
        <input type="submit" />
      </form>
      <br />
      <div id="canvas-div">
        <img id="canvas-bg" src={file} />
        <canvas id="covering-canvas"></canvas>
        <Helmet>
          <script type="text/javascript">
            {`
            var canvas = document.getElementById('covering-canvas');
            // Make it visually fill the positioned parent
            // canvas.style.width ='100%';
            // canvas.style.height='100%';
            // ...then set the internal size to match
            canvas.width  = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            var ctx = canvas.getContext('2d');
            //Variables
            var canvasx = $(canvas).offset().left;
            var canvasy = $(canvas).offset().top;
            var last_mousex = last_mousey = 0;
            var mousex = mousey = 0;
            var mousedown = false;
            
            //Mousedown
            $(canvas).on('mousedown', function(e) {
                last_mousex = parseInt(e.clientX-canvasx);
                last_mousey = parseInt(e.clientY-canvasy);
                mousedown = true;
            });
            
            //Mouseup
            $(canvas).on('mouseup', function(e) {
                mousedown = false;
            });
            
            //Mousemove
            $(canvas).on('mousemove', function(e) {
                mousex = parseInt(e.clientX-canvasx);
                mousey = parseInt(e.clientY-canvasy);
                if(mousedown) {
            ctx.clearRect(0,0,canvas.width,canvas.height); //clear canvas
            ctx.beginPath();
            var width = mousex-last_mousex;
            var height = mousey-last_mousey;
            ctx.rect(last_mousex,last_mousey,width,height);
            ctx.strokeStyle = 'red';
            ctx.lineWidth = 1;
            ctx.stroke();
                }
                //Output
                console.log('current: '+mousex+', '+mousey+'<br/>last: '+last_mousex+', '+last_mousey+'<br/>mousedown: '+mousedown);
            });`}
          </script>
        </Helmet>
      </div>
      <img id="outimg" src="" />
      <br />
      <button onClick={download}>Download</button>
    </div>
  );
}

export default Crop;
