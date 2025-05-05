document.addEventListener("DOMContentLoaded", ()=>{
  const form   = document.getElementById("form");
  const birth  = document.getElementById("birth");
  const result = document.getElementById("result");

  form.addEventListener("submit", async e=>{
    e.preventDefault();
    const date = birth.value;
    if(!date){ return; }

    try{
      const rsp  = await fetch("/api/phase",{
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body: JSON.stringify({ date })
      });
      const data = await rsp.json();

      if(data.success){
        result.innerHTML = `
          <h3>${data.title}</h3>
          <p>${data.text}</p>
          <div class="mantra">${data.mantra}</div>`;
      }else{
        result.innerHTML = `<span style="color:red;">${data.error}</span>`;
      }
      result.style.display = "block";
    }catch(err){
      result.innerHTML = "<span style='color:red;'>Ошибка связи с сервером</span>";
      result.style.display = "block";
    }
  });
});
