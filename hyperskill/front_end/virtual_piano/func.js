document.addEventListener('keydown', function (event){
    if (event.code == "KeyA"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/A.mp3";
        audio.play()
    }
    else if (event.code == "KeyS"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/S.mp3";
        audio.play()
    }
    else if (event.code == "KeyD"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/D.mp3";
        audio.play()
    }

    else if (event.code == "KeyF"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/F.mp3";
        audio.play()
    }

    else if (event.code == "KeyG"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/G.mp3";
        audio.play()
    }
    
    else if (event.code == "KeyH"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/H.mp3";
        audio.play()
    }
    else if (event.code == "KeyJ"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "white_keys/J.mp3";
        audio.play()
    }
    else if (event.code == "KeyW"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "black_keys/W.mp3";
        audio.play()
    }
    else if (event.code == "KeyE"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "black_keys/E.mp3";
        audio.play()
    }
    else if (event.code == "KeyT"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "black_keys/T.mp3";
        audio.play()
    }
    else if (event.code == "KeyY"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "black_keys/Y.mp3";
        audio.play()
    }
    else if (event.code == "KeyU"){
        let audio = document.createElement("AUDIO");
        let src = audio.src;
        audio.src = "black_keys/U.mp3";
        audio.play()
    }
    else {
        console.log("Warning! Wrong key");
    }
});
