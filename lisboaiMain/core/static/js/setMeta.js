var currentUrl = document.URL;

var properties = {url:currentUrl,
    type:"Website", 
    title: {{post.title}}, 
    description: {{post.short_description}},
    image:"{{post.image}}"  
    }

    console.log(properties)
    for(var i=0;i<= properties.length; i++){

        var link = document.createElement('meta');
        link.setAttribute('property', 'og:'+ Object.keys(properties));
        link.content = Object.values(properties);
        document.getElementsByTagName('head')[0].appendChild(link);

        console.log(link)
        
    }


