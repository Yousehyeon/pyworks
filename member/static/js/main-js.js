window.onload = function(){
    // 디지털 시계
    setInterval(setWatch, 1000);

    function setWatch(){
        let date = new Date()
        let now = date.toLocaleTimeString();
        document.getElementById('demo').innerHTML = now
    }

    // 배경 이미지 슬라이딩
    let picture = [
    "../static/images/bg1.jpg",
    "../static/images/bg2.jpg",
    "../static/images/bg3.jpg"
    ]

    let imgIdx = 0;

    showPicture();

    function showPicture(){
        let img = document.getElementByID('pic');
        img.src = picture[imgIdx]
        imgIdx++;
        if(imgIdx == picture.length){
            imgIdx =0;
        }

        setTimeout(showPicture, 2000);
    }
}