/* =========================================================
   main.js — progressive enhancement only.
   The site is fully usable with JS disabled: nav links work,
   the form still submits (to mailto fallback / server action).
   ========================================================= */
(function () {
  'use strict';

  /* ---- Footer year (falls back to the static markup value if JS is off) ---- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---- Mobile navigation toggle ---- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-navigation');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Close the mobile menu with Escape, and return focus to the toggle
    // so keyboard users are not stranded inside a hidden menu.
    nav.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---- Accessible contact form validation ---- */
  var form = document.getElementById('contact-form');
  if (!form) return;

  var statusBox = document.getElementById('form-status');

  var validators = {
    name: function (value) {
      return value.trim().length > 0 ? '' : 'Enter your full name.';
    },
    email: function (value) {
      if (value.trim().length === 0) return 'Enter your email address.';
      var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return pattern.test(value.trim()) ? '' : 'Enter a valid email address, e.g. name@example.com.';
    },
    subject: function (value) {
      return value.trim().length > 0 ? '' : 'Enter a subject.';
    },
    message: function (value) {
      return value.trim().length > 0 ? '' : 'Enter a message.';
    }
  };

  function setFieldError(fieldName, message) {
    var input = form.elements[fieldName];
    var wrapper = input.closest('.field');
    var errorEl = document.getElementById(fieldName + '-error');

    if (message) {
      wrapper.classList.add('has-error');
      input.setAttribute('aria-invalid', 'true');
      if (errorEl) errorEl.textContent = message;
    } else {
      wrapper.classList.remove('has-error');
      input.setAttribute('aria-invalid', 'false');
      if (errorEl) errorEl.textContent = '';
    }
  }

  function validateField(fieldName) {
    var input = form.elements[fieldName];
    var message = validators[fieldName](input.value);
    setFieldError(fieldName, message);
    return message === '';
  }

  // Validate on blur so errors appear as the person moves through
  // the form, not only on submit.
  Object.keys(validators).forEach(function (fieldName) {
    var input = form.elements[fieldName];
    if (!input) return;
    input.addEventListener('blur', function () {
      validateField(fieldName);
    });
  });

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    var fieldNames = Object.keys(validators);
    var allValid = true;
    var firstInvalid = null;

    fieldNames.forEach(function (fieldName) {
      var valid = validateField(fieldName);
      if (!valid) {
        allValid = false;
        if (!firstInvalid) firstInvalid = form.elements[fieldName];
      }
    });

    statusBox.classList.remove('success', 'error');

    if (!allValid) {
      statusBox.textContent = 'The form has errors. Please review the highlighted fields before submitting.';
      statusBox.classList.add('error', 'is-visible');
      statusBox.setAttribute('role', 'alert');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    // No backend is connected in this static build, so we confirm
    // locally and hand off to the mailto link as a working fallback.
    statusBox.textContent = 'Thanks — your message is ready to send. Your email app should now open with the details filled in.';
    statusBox.classList.add('success', 'is-visible');
    statusBox.setAttribute('role', 'status');

    var name = encodeURIComponent(form.elements.name.value.trim());
    var subject = encodeURIComponent(form.elements.subject.value.trim());
    var body = encodeURIComponent(
      form.elements.message.value.trim() + '\n\n— ' + name + ' (' + form.elements.email.value.trim() + ')'
    );
    window.location.href = 'mailto:poojan80500@gmail.com?subject=' + subject + '&body=' + body;

    form.reset();
  });
})();
