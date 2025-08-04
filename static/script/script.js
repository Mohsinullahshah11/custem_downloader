async function splitPDF() {
  let youtube_url = document.getElementById('youtube-url').value;
  let download_type = document.getElementById('download-type').value;
  let download_formet = document.getElementById('download-format').value;


  // Build query string
const params = new URLSearchParams({
  youtube_url: youtube_url,
  download_type: download_type,
  download_formet: download_formet
});

const downloadUrl = `/api/download?${params.toString()}`;

// Trigger native download via <a> (so progress shows in browser)
const a = document.createElement('a');
a.href = downloadUrl;
a.download = ''; // Optional: browser uses filename from server
document.body.appendChild(a);
a.click();
a.remove();


  // const contentDisposition = response.headers.get('Content-Disposition');
  // let filename = 'downloaded_file.zip';  // default
  // if (contentDisposition && contentDisposition.includes('filename=')) {
  //   const match = contentDisposition.match(/filename="?(.+?)"?$/);
  //   if (match) filename = match[1];
  // }

  
  // const a = document.createElement('a');
  // a.href = url;
  // a.download = filename;
  // document.body.appendChild(a);
  // a.click();
  // a.remove();

  // window.URL.revokeObjectURL(url);




}

const submitbtn = document.getElementById('submit');

submitbtn.addEventListener('click', (e) => {
  // e.preventDefault();
  splitPDF();
});