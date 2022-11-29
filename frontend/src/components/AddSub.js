// Importing modules
import React, { useRef, useState } from "react";
import { saveAs } from "file-saver";
import "../App.css"

function AddSub() {
  const form = useRef(null);
  const [file1, setFile1] = useState();
  const [file2, setFile2] = useState();

  const submit = (e) => {
    e.preventDefault();
    const primary_image = document.querySelector("#primary_image");
    const data =
      primary_image.files.length == 0 ? [] : new FormData(form.current);
      // console.log(data.current.get("photo1"));

      data.set(e.target.name, e.target.value);
    fetch("/addSub", {
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

  function preview1(e) {
    setFile1(URL.createObjectURL(e.target.files[0]));
  }
  function preview2(e) {
    setFile2(URL.createObjectURL(e.target.files[0]));
  }

  return (
    <div>
      <h3>Addition and Subtraction of Two Images</h3>
      <form ref={form} onSubmit={submit}>
        <input
          id="primary_image"
          type="file"
          accept="image/*"
          name="photo1"
          onChange={preview1}
        />
        <input
          id="primary_image"
          type="file"
          accept="image/*"
          name="photo2"
          onChange={preview2}
        />
        <button name="action" value="add" onClick={submit}>
          Add
        </button>
        <button name="action" value="subtract" onClick={submit}>
          Subtract
        </button>
      </form>
      <img className="img2" id="frame1" src={file1} />
      <img className="img2" id="frame2" src={file2} />
      <img className="img2" id="outimg" src="" />
      <br />
      <button onClick={download}>Download</button>
    </div>
  );
}

export default AddSub;
