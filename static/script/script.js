async function splitPDF() {
  let youtube_url = document.getElementById('youtube-url').value;
  let download_type = document.getElementById('download-type').value;
  let download_formet = document.getElementById('download-format').value;


  const formData = new FormData();
  formData.append('youtube_url', youtube_url);
  formData.append('download_type', download_type);
  formData.append('download_formet', download_formet);

  // console.log(formData['form']);


  // try {
    const response = await fetch('/api/download', {
      method: 'POST',
      body: formData 
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    console.log(`url ${url}`)
    a.download
    document.body.appendChild(a);
    a.click();
    a.remove();

    window.URL.revokeObjectURL(url);

  


}

const submitbtn = document.getElementById('submit');

submitbtn.addEventListener('click', (e) => {
  // e.preventDefault();
  splitPDF();
});