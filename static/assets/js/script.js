/*-----------------------------------------------------------------------------------

 Template Name: Fastkart
 Template URI: themes.pixelstrap.com/Fastkart
 Description: This is Ecommerce website
 Author: Pixelstrap
 Author URI: https://themeforest.net/user/pixelstrap

 ----------------------------------------------------------------------------------- */

// 01. Image to background js
// 02. Shop Page Grid Setting Js
// 03. Footer function js
// 04. mobile menu active class js
// 05. btn-cart open close js
// 06. quantity js
// 07. Tap to Top js
// 08. User Dashboard Left Sidebar Show js
// 09. Tooltip js
// 10. Cookie Bar js
// 11. Image To Background js
// 12. search box function Js
// 13. Wishlist Js
// 14. Loader Js
// 15. header Dropdown Js
// 16. Add to Cart Show Js
// 17. active class Js
// 18. Scroll down header fix js
// 19. setting - option open js
// 20. user-dashboard profile change js
// 21. Wishlist box remove js
// 22. Category Box js
// 23. remove notication bar js
// 24. category box js

(function ($) {
    "use strict";
    /*=====================
    01. Image to background js
    ==========================*/
    $(".bg-top").parent().addClass("b-top");
    $(".bg-bottom").parent().addClass("b-bottom");
    $(".bg-center").parent().addClass("b-center");
    $(".bg-left").parent().addClass("b-left");
    $(".bg-right").parent().addClass("b-right");
    $(".bg_size_content").parent().addClass("b_size_content");
    $(".bg-img").parent().addClass("bg-size");
    $(".bg-img.blur-up").parent().addClass("blur-up lazyload");
    $(".bg-img").each(function () {
        var el = $(this),
            src = el.attr("src"),
            parent = el.parent();

        parent.css({
            "background-image": "url(" + src + ")",
            "background-size": "cover",
            "background-position": "center",
            "background-repeat": "no-repeat",
            display: "block",
        });

        el.hide();
    });

    /*=====================
    02. Shop Page Grid Setting Js
    ==========================*/
    $(".grid-option li").on("click", function () {
        $(this).addClass('active').siblings().removeClass('active');
    });
    $(".grid-option .grid-btn").on("click", function () {
        $(".product-list-section").removeClass("list-style");
    });
    $(".grid-option .list-btn").on("click", function () {
        $(".product-list-section").addClass("list-style");
    });
    $('.three-grid').on('click', function (e) {
        $(".product-list-section").removeClass("row-cols-xxl-5 row-cols-xxl-4 row-cols-xl-3 row-cols-lg-2 row-cols-md-3 row-cols-2 list-style").addClass("row-cols-xl-3 row-cols-lg-2 row-cols-md-3 row-cols-2");
    });
    $('.grid-btn').on('click', function (e) {
        $(".product-list-section").removeClass("row-cols-xxl-5 row-cols-xxl-4 row-cols-xl-3 row-cols-lg-2 row-cols-md-3 row-cols-2 list-style").addClass("row-cols-xxl-4 row-cols-xl-3 row-cols-lg-2 row-cols-md-3 row-cols-2");
    });
    $('.five-grid').on('click', function (e) {
        $(".product-list-section").removeClass("list-style").addClass("row-cols-xxl-5 row-cols-xl-3 row-cols-lg-2 row-cols-md-3 row-cols-2");
    });
    var contentwidth = $(window).width();
    if (contentwidth < "1199") {
        $(".grid-options ul .grid-btn").addClass("active");
    }
    if (contentwidth < "1399") {
        $(".grid-options ul .three-grid").addClass("active");
    }
})(jQuery);

/*=====================
    03. Footer function js
==========================*/
var contentwidth = $(window).width();
if (contentwidth < "576") {
    $(".footer-title h4").append(
        '<span class="according-menu float-end"><i class="fa-solid fa-angle-down"></i></span>'
    );
    $(".footer-title").on("click", function () {
        $(".footer-title")
            .removeClass("active")
            .find("span")
            .replaceWith(
                '<span class="according-menu float-end"><i class="fa-solid fa-angle-down"></i></span>'
            );
        $(".footer-contact, .footer-contain").slideUp("normal");
        if ($(this).next().is(":hidden") == true) {
            $(this).addClass("active");
            $(this)
                .find("span")
                .replaceWith(
                    '<span class="according-menu float-end"><i class="fas fa-chevron-up"></i></span>'
                );
            $(this).next().slideDown("normal");
        } else {
            $(this)
                .find("span")
                .replaceWith(
                    '<span class="according-menu float-end"><i class="fa-solid fa-angle-down"></i></span>'
                );
        }
    });
    $(".footer-contact, .footer-contain").hide();
} else {
    $(".footer-contact, .footer-contain").show();
}

/*=====================
  04. mobile menu active class js
   ==========================*/
$(document).ready(function () {
    $('.mobile-menu ul li a').click(function () {
        $('li a').removeClass("active");
        $(this).addClass("active");
    });
});

/*=====================
  05. btn-cart open close js
   ==========================*/
$(document).ready(function () {
    $('.button-item').on("click", function () {
        $('.item-section').addClass("active");
    });

    $('.close-button').on("click", function () {
        $('.item-section').removeClass("active");
    });

    $('.btn-cart').on("click", function () {
        setTimeout(function () {
            $('.item-section').addClass("active")
        }, 1500);
        setTimeout(function () {
            $('.item-section').removeClass('active');
        }, 5000);
    });
});

/*=====================
  06. quantity js
   ==========================*/
$('.qty-box .quantity-right-plus').on('click', function () {
    var $qty = $(this).parents(".qty-box").find(".input-number");
    var currentVal = parseInt($qty.val(), 10);
    if (!isNaN(currentVal)) {
        $qty.val(currentVal + 0);
    }
});
$('.qty-box .quantity-left-minus').on('click', function () {
    var $qty = $(this).parents(".qty-box").find(".input-number");
    var currentVal = parseInt($qty.val(), 10);
    if (!isNaN(currentVal) && currentVal > 0) {
        $qty.val(currentVal - 0);
    }
});

/*=====================
  07. Tap to Top js
   ==========================*/
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('.back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });
});

/*=====================
   08. User Dashboard Left Sidebar Show Js
   ==========================*/
$(".left-dashboard-show").click(function () {
    $(".dashboard-left-sidebar").addClass("show");
});
$(".close-button, .bg-overlay, .user-nav-pills .nav-item .nav-link").click(function () {
    $(".bg-overlay, .dashboard-left-sidebar").removeClass("show");
});

/*=====================
   09. Tooltip Js
   ==========================*/
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

/*=====================
   10. Cookie Bar Js
   ==========================*/
$(".ok-button").click(function () {
    $(".cookie-bar-box").addClass("hide");
});

/*=====================
   11. Image To Background Js
   ==========================*/
$(".bg-top").parent().addClass("b-top");
$(".bg-bottom").parent().addClass("b-bottom");
$(".bg-center").parent().addClass("b-center");
$(".bg-left").parent().addClass("b-left");
$(".bg-right").parent().addClass("b-right");
$(".bg_size_content").parent().addClass("b_size_content");
$(".bg-img").parent().addClass("bg-size");
$(".bg-img.blur-up").parent().addClass("blur-up lazyload");
$(".bg-img").each(function () {
    var el = $(this),
        src = el.attr("src"),
        parent = el.parent();

    parent.css({
        "background-image": "url(" + src + ")",
        "background-size": "cover",
        "background-position": "center",
        "background-repeat": "no-repeat",
        display: "block",
    });

    el.hide();
});

/*=====================
   12. search box function Js
   ==========================*/
$(".search-box").on("click", function () {
    $(this).closest(".rightside-box").find(".search-full").addClass("open");
});
$(window).on("load resize", function () {
    // open searchbox
    $(".search-type").on("click", function () {
        $(this).parents(".search-full").addClass("show");
    });

    // close seach
    $(".close-search").on("click", function () {
        $(this).closest(".rightside-box").find(".search-full").removeClass("open");
    });
});

/*=====================
   13. Wishlist Js
   ==========================*/
$(".notifi-wishlist").on("click", function () {
    $.notify({
        icon: "fa fa-check",
        title: "Success!",
        message: "Item Successfully added in wishlist",
    }, {
        element: "body",
        position: null,
        type: "info",
        allow_dismiss: true,
        newest_on_top: false,
        showProgressbar: true,
        placement: {
            from: "top",
            align: "right",
        },
        offset: 20,
        spacing: 10,
        z_index: 1031,
        delay: 5000,
        animate: {
            enter: "animated fadeInDown",
            exit: "animated fadeOutUp",
        },
        icon_type: "class",
        template: '<div data-notify="container" class="col-xxl-3 col-lg-5 col-md-6 col-sm-7 col-12 alert alert-{0}" role="alert">' +
            '<button type="button" aria-hidden="true" class="btn-close" data-notify="dismiss"></button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
            '<div class="progress-bar progress-bar-info progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            "</div>" +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
            "</div>",
    });
});

$(".cart-add").on("click", function () {
    $.notify({
        icon: "fa fa-check",
        title: "Success!",
        message: "Item Successfully added to Cart",
    }, {
        element: "body",
        position: null,
        type: "info",
        allow_dismiss: true,
        newest_on_top: false,
        showProgressbar: true,
        placement: {
            from: "top",
            align: "right",
        },
        offset: 20,
        spacing: 10,
        z_index: 1031,
        delay: 5000,
        animate: {
            enter: "animated fadeInDown",
            exit: "animated fadeOutUp",
        },
        icon_type: "class",
        template: '<div data-notify="container" class="col-xxl-3 col-lg-5 col-md-6 col-sm-7 col-12 alert alert-{0}" role="alert">' +
            '<button type="button" aria-hidden="true" class="btn-close" data-notify="dismiss"></button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
            '<div class="progress-bar progress-bar-info progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            "</div>" +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
            "</div>",
    });
});

/*=====================
   14. Loader Js
   ==========================*/
const loaderEl = document.getElementsByClassName("fullpage-loader")[0];
document.addEventListener("readystatechange", (event) => {
    const readyState = "complete";
    if (document.readyState == readyState) {
        loaderEl.classList.add("fullpage-loader--invisible");

        setTimeout(() => {
            loaderEl.parentNode.removeChild(loaderEl);
        }, 100);
    }
});

/*=====================
    15. header Dropdown Js
 ==========================*/
$(".dropdown-menu li a").on('click', function () {
    var a = $(this).closest("a");
    var getSampling = a.text();
    var getImage = a.find('img').attr('src');

    // console.log("src path", getImage);
    $(this).closest(".dropdown-menu").prev('.dropdown-toggle').find('span').text(getSampling);
    $(this).closest(".dropdown-menu").prev('.dropdown-toggle').find('img').attr("src", getImage);
});

/*=====================
   16. Add to Cart Show Js
   ==========================*/
$(".addCart").click(function () {
    $(".add-cart-box").addClass("show");
    setTimeout(function () {
        $(".add-cart-box").removeClass("show");
    }, 5000);
});
$(".add-cart-box .btn-close").click(function () {
    $(".add-cart-box").removeClass("show");
});

/*=====================
   17. active class Js
   ==========================*/
$(".product-packege .select-packege li a").click(function () {
    $("li a").removeClass("active");
    $(this).addClass("active");
});

/*=====================
   18. Scroll down header fix js
   ==========================*/
$(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $('header').addClass('active')
    } else {
        $('header').removeClass('active')
    }
});

/*=====================
   19. setting-option open js
   ==========================*/
$(".theme-option .setting-box .setting-button").click(function () {
    $(".theme-setting-2").toggleClass("active");
    $(this).find("i").toggleClass("fa-xmark");
});

/*=====================
   20. user-dashboard profile change js
   ==========================*/
function readURL(uploader) {
    $('.update_img').attr('src',
        window.URL.createObjectURL(uploader.files[0]));
};

/*=====================
   21. Wishlist box remove js
   ==========================*/
$(".close_button").click(function () {
    $(this).closest(".product-box-contain").fadeOut("slow", function () {
        $(this).closest(".product-box-contain").remove();
    });
});

/*=====================
   22. Category Box js
   ==========================*/
$(".mobile-category").click(function () {
    $(".bg-overlay, .category-dropdown").addClass("show");
});
$(".close-button, .bg-overlay").click(function () {
    $(".bg-overlay, .category-dropdown").removeClass("show");
});

/*=====================
   23. remove notication bar js
   ==========================*/
$(".close-notification").click(function () {
    $(".header-notification").addClass("remove");
});

/*=====================
    24. category box js
==========================*/
var contentwidth = $(window).width();
if (contentwidth < "767") {
    $(".onhover-category-list .category-name").append('<span class="according-menu">+</span>');
    $(".category-name").on("click", function () {
        $(".category-name")
            .removeClass("active")
            .find("span")
            .replaceWith('<span class="according-menu">+</span>');
        $(".onhover-category-list .onhover-category-box").slideUp("normal");
        if ($(this).next().is(":hidden") == true) {
            $(this).addClass("active");
            $(this)
                .find("span")
                .replaceWith('<span class="according-menu">-</span>');
            $(this).next().slideDown("normal");
        } else {
            $(this)
                .find("span")
                .replaceWith('<span class="according-menu">+</span>');
        }
    });
    $(".accordion-box").hide();
}

/*=====================
   25. Sidebar Hide & Show Js
   ==========================*/
$(".navbar-toggler-icon-2").click(function () {
    $(".bg-overlay, .sidebar-col").addClass("show");
});
$(".bg-overlay").click(function () {
    $(".bg-overlay, .sidebar-col").removeClass("show");
});

$(".show-button").click(function () {
    $(".left-box, .wow, .fadeInUp").addClass("show");
});

$(".left-box").click(function () {
    $(".left-box, .wow, .fadeInUp").removeClass("show");
});


$(".choose-size").on('click',function(){
    var _vm= $(this);
    var _id=_vm.attr('data-select');
    $(".choose-size").removeClass('prod-size-'+_id);
    $(".dis-price").hide();
    $(this).addClass('prod-size-'+_id);

    var _price=$(this).attr('data-price');
    $(".product-price").text(_price);
    $(".product-price-h").val(_price);
})

$(document).on('click', ".add-to-cart",function(){
    var _vm= $(this);
    var _index=_vm.attr('data-index');
    var _qty= $(".prod-qty-"+_index).val();
    var _productId= $(".prod-id-"+_index).val();
    var _productImage= $(".prod-image-"+_index).val();
    var _productColor= $(".prod-color-"+_index).val();
    var _productSize= $(".prod-size-"+_index).text();
    var _productTitle= $(".prod-name-"+_index).val();
    var _productRef= $(".prod-ref-"+_index).val();
    var _productCategory= $(".prod-cat-"+_index).val();
    var _productVendor= $(".prod-vendor-"+_index).val();
    var _productPrice= $(".prod-price-"+_index).val();
    var _productStock= $(".prod-stock-"+_index).val();
    
    //Ajax
    $.ajax({
        url:'/add-to-cart/',
        data:{
            'id':_productId,
            'img':_productImage,
            'qty':_qty,
            'title':_productTitle,
            'ref':_productRef,
            'color':_productColor,
            'size':_productSize,
            'price':_productPrice,
            'cat':_productCategory,
            'vendor':_productVendor,
            'stock':_productStock,
            
        },
        dataType:'json',
        beforeSend:function(){
            _vm.attr('disabled',true);
        },
        success:function(res){
            $(".cartlist").text(res.totalitems);
            $(".cart-total").text(res.total_amt);
            _vm.attr('disabled',false);
        }
    });
});


// Delete item from cart
$(document).on('click','.delete-item',function(){
    var _pId=$(this).attr('data-item');
    var _vm=$(this);
    // Ajax
    $.ajax({
        url:'/delete-from-cart',
        data:{
            'id':_pId,
        },
        dataType:'json',
        beforeSend:function(){
            _vm.attr('disabled',true);
        },
        success:function(res){
            $(".cart-list").text(res.totalitems);
            _vm.attr('disabled',false);
            $("#cartList").html(res.data);
        }
    });
    // End
});

// Update item from cart
$(document).on('click','.update-item',function(){
    var _pId=$(this).attr('data-item');
    var _pQty=$(".prod-qty-"+_pId).val();
    var _pPrice= $(".prod-price-"+_pId).val();
    var _pSize=$(".prod-size-"+_pId).text();
    var _pStock= $(".prod-stock-"+_pId).val();
    var _vm=$(this);
    // Ajax
    $.ajax({
        url:'/update-cart',
        data:{
            'id':_pId,
            'qty':_pQty,
            'size':_pSize,
            'price':_pPrice,
            'stock':_pStock,
        },
        dataType:'json',
        beforeSend:function(){
            _vm.attr('disabled',true);
        },
        success:function(res){
            // $(".cart-list").text(res.totalitems);
            _vm.attr('disabled',false);
            $("#cartList").html(res.data);
        }
    });
    // End
});


// delivery 
$(document).on('click', '.location',function() {
  var _pId=$(this).attr('data-item');
  var _city=$(".loc_price-"+_pId).text();
  var _subtotal=$(".sub_price").val();
  var _discount=$(".code_price").val();

  $.ajax({                     
    url: '/delivery_price',  
    data: {
      'city': _city,
      'subtotal': _subtotal,
      'discount': _discount, 
    },
    success: function (data) {   
      $("#del_price").html(data); 
    }
  });

});


// Add wishlist
    $(document).on('click',".add-wishlist",function(){
        var _pid=$(this).attr('data-product');
        var _vm=$(this);
        // Ajax
        $.ajax({
            url:"/add-wishlist",
            data:{
                product:_pid
            },
            dataType:'json',
            success:function(res){
                if(res.bool==true){
                    _vm.addClass('disabled').removeClass('add-wishlist');
                }
            }
        });
        // EndAjax
    });
    // End

$(".printord").click(function() {
        window.print()
});

$(document).on('click', '#prod_cat',function() {

      var prod_id = $(this).val();

      $.ajax({                     
        url: '/shop/subcat',  
        data: {
          'id': prod_id   
        },
        success: function (data) {   
          $("#prod_sub_cat").html(data); 
        }
      });

});


// Check password validity

$(document).ready(function() {
  var passwordInput = $('input[name="password1"]');
  var passwordLengthMessage = $('#password-length-message');
  var passwordValidityMessage = $('#password-validity-message');

  // Check password length
  passwordInput.on('input', function() {
    var password = $(this).val();
    if (password.length < 8) {
      passwordLengthMessage.show();
    } else {
      passwordLengthMessage.hide();
    }
  });

  // Check password validity
  passwordInput.on('input', function() {
    var password = $(this).val();
    var hasUppercase = /[A-Z]/.test(password);
    var hasLowercase = /[a-z]/.test(password);
    var hasNumber = /\d/.test(password);
    var hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password);
    if (hasUppercase && hasLowercase && hasNumber && hasSpecial) {
      passwordValidityMessage.hide();
    } else {
      passwordValidityMessage.show();
    }
  });
});

//Check confirm password

$(document).ready(function() {
  // Listen for changes in the password and confirm password fields
  $('#password1, #password2').on('keyup', function() {
    var password = $('#password1').val();
    var confirm_password = $('#password2').val();
    // Compare the two values and show an error message if they don't match
    if (password != confirm_password) {
      $('#password2').addClass('is-notvalid');
      $('#password-help').html('Passwords do not match.');
    } else {
      $('#password2').removeClass('is-notvalid');
      $('#password-help').html('');
    }
  });
});

