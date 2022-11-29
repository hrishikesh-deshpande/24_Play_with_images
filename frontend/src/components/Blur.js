// Importing modules
import React, { useRef, useState } from "react";
import { saveAs } from "file-saver";

function Blur() {
  const form = useRef(null);
  const [file, setFile] = useState();

  const submit = (e) => {
    e.preventDefault();
    const primary_image = document.querySelector("#primary_image");
    const data =
      primary_image.files.length == 0 ? [] : new FormData(form.current);
    fetch("/blur", {
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
      <h3>Upload an image to apply Blur filter</h3>
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
      <img id="frame" src={file} />
      <img id="outimg" src="" />
      <br />
      <button onClick={download}>Download</button>
    </div>
  );
}

export default Blur;
