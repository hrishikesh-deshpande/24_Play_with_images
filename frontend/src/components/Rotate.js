// Importing modules
import React, { useRef, useState } from "react";
import { saveAs } from "file-saver";

function Rotate() {
  const form = useRef(null);
  let data = useRef();
  const [i, setI] = useState(0);
  const [file, setFile] = useState();

  const submit = (e) => {
    e.preventDefault();
    if (i == 0) {
      data.current = new FormData(form.current);
      setI(i + 1);
    }
    data.current.set(e.target.name, e.target.value);
    fetch("/rotate", {
      method: "POST",
      body: data.current,
      encType: "multipart/form-data",
    })
      .then((res) => res.json())
      .then((json) => {
        if (json.status != 200) {
          console.log(json.message);
          return;
        }
        fetch(`data:image/jpg;base64, ${json.processed_image}`)
          .then((res) => res.blob())
          .then(
            (blob) => new File([blob], "FileName.jpg", { type: "image/jpg" })
          )
          .then((file1) => {
            data.current.set("photo", file1);
          });
        setFile(`data:image/jpg;base64, ${json.processed_image}`);
      });
  };

  const download = () => {
    const outimgsrc = document.getElementById("frame").getAttribute("src");
    if (outimgsrc) saveAs(outimgsrc, "imagical.jpg");
    else alert("No output generated");
  };

  function preview(e) {
    setFile(URL.createObjectURL(e.target.files[0]));
  }

  return (
    <div>
      <h3>Upload an image to Rotate</h3>
      <form ref={form} onSubmit={submit}>
        <input
          id="input-img"
          type="file"
          accept="image/*"
          name="photo"
          onChange={preview}
        />
        <button name="direction" value="left" onClick={submit}>
          left
        </button>
        <button name="direction" value="right" onClick={submit}>
          right
        </button>
      </form>
      <img id="frame" src={file} />
      <br />
      <button onClick={download}>Download</button>
    </div>
  );
}

export default Rotate;
