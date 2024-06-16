//" I pledge my honor that I have abided by the Stevens Honor System" - Himanshu Rana 
// Keep this for the students
var fileLocations = {
	woofer: 'assets/woofer.jpg',
	pupper: 'assets/pupper.jpg',
	clouds: 'assets/clouds.jpg',
	snek: 'assets/snek.jpg'
};

/**
 * This function will get the values of the following elements:
 * 		input-username, input-caption, input-picture
 * Then, this will pass those values to the addNewPost function.
 * 
 */
function handleFormSubmit() {
	if(window.event) window.event.preventDefault(); 
	var inputUsername = document.getElementById("input-username").value;
	var inputCaption  = document.getElementById("input-caption").value;
	var inputPicture  = document.getElementById("input-picture").value;
    addNewPost(inputUsername, fileLocations[inputPicture], inputCaption);
}

/**
 * This function create the following div and append it to the #post-list element
	<div class="post">
		<span>{username}</span>
		<img src="{img_src}" alt="{caption}">
		<div id="post-overlay">
			{caption}
		</div>
	</div>
 * 
 * Also, add a mouseover and mouseleave events to the post div for opacity 
 * transitions in the post-overlay div
 */
function addNewPost(username, img_src, caption) {
	// Create the parent post div
    var node = document.createElement("div"); 
    node.className = "post"; 
    
	// Create a span for the user
    var span  = document.createElement("span");
    span.appendChild(document.createTextNode(username));
    
	// Create image element
    var image = document.createElement("img"); 
    image.src = img_src; 
    image.alt = caption;
    
   
    
	// Create overlay element
    var overlay = document.createElement("div"); 
    overlay.appendChild(document.createTextNode(caption));
    overlay.id = "post-overlay"; 

	// Add all child elements (order matters)
    node.appendChild(span);
    node.appendChild(image);
    node.appendChild(overlay);
    
	// Add event listeners to post
    node.addEventListener("mouseover", function() {
        overlay.style.transition = "opacity 0.5s";
        overlay.style.opacity = "1";                                           }
                         );
     node.addEventListener("mouseout", function() {overlay.style.transition = "opacity 0.5s";
     overlay.style.opacity = "0";                                           }
                         );
                        
	// Add post element to post list
    document.getElementById("post-list").appendChild(node);
    
   
   
    
    
}

