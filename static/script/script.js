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

  const contentDisposition = response.headers.get('Content-Disposition');
  let filename = 'downloaded_file.zip';  // default
  if (contentDisposition && contentDisposition.includes('filename=')) {
    const match = contentDisposition.match(/filename="?(.+?)"?$/);
    if (match) filename = match[1];
  }

  // Create a stream and download it natively
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
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