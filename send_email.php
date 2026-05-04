<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "support@whatsthetimeworld.com";
    $subject = "New Project Quote Request from " . $_POST['name'];
    
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $plan = strip_tags(trim($_POST["plan"]));
    $message = strip_tags(trim($_POST["message"]));

    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Plan: $plan\n\n";
    $email_content .= "Message:\n$message\n";

    $headers = "From: $name <$email>";

    if (mail($to, $subject, $email_content, $headers)) {
        // Redirect to a thank you message or back to the home page with a success flag
        header("Location: whatsthetime.html?status=success#contact-form");
    } else {
        header("Location: whatsthetime.html?status=error#contact-form");
    }
} else {
    header("Location: whatsthetime.html");
}
?>
