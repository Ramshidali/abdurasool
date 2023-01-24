function product_onload_ajax() {
    f_child = $(".services-slider li.first-category-li").attr("id").replace('li','')
    id = "li"+f_child;
    category = f_child
    url = $("#"+id).attr("data-url");

    // console.log("category=== "+category);
    // console.log("category id=== "+id);
    // console.log("url=== "+url);

    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        data: {
            category: category,
        },

        success: function (data) {
            products = data["product_instances"]
            c_description_title = data["c_desctription_title"]
            c_description_description = data["c_desctription_description"]

            let html_content = ""
            for (i=0;i<products.length;i++){
                product = products[i]
                html_content += `
                    <li>
                        <a href="#">
                            <span ><img src="${product["image"]}" alt="${product["name"]}" /></span>
                            <div class="info">
                                <h5>${product["name"]}</h5>
                                <p>${product["color"]}</p>
                            </div>
                        </a>
                    </li>
                `
            }
            $("#designs .slider-item").html(html_content)

            $("#cat_description_title").html(c_description_title)
            $("#cat_description_description").html(c_description_description)
        },

        error: function (data) {
            // console.log("no products");
        },
    });
}


function product_ajax(category) {
    id = "li"+category;
    url = $("#"+id).attr("data-url");

    // console.log("category=== "+category);
    // console.log("category id=== "+id);
    // console.log("url=== "+url);

    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        data: {
            category: category,
        },

        success: function (data) {
            products = data["product_instances"]
            c_description_title = data["c_desctription_title"]
            c_description_description = data["c_desctription_description"]
            let html_content = ""

            if(products){
                for (i=0;i<products.length;i++){
                    product = products[i]
                    html_content += `
                        <li>
                            <a href="#">
                                <span ><img src="${product["image"]}" alt="${product["name"]}" /></span>
                                <div class="info">
                                    <h5>${product["name"]}</h5>
                                    <p>${product["color"]}</p>
                                </div>
                            </a>
                        </li>
                    `
                }
                $("#designs .slider-item").html(html_content)

                $("#cat_description_title").html(c_description_title)
                $("#cat_description_description").html(c_description_description)
            }


        },

        error: function (data) {
            // console.log("no products");
        },
    });
}