title: Using Tailwind CSS with Render-Engine
slug: tailwind-x-render-engine
date: 28 Aug 2020 15:00

Tailwind CSS is a CSS Framework that is growing in massive popularity. It
features an _easy-to-use_, _start-from-zero_, approach to adding style to your
website.

Tailwind has been easily integrated into many javascript frameworks, including
the static ones. It's just as easy to apply tailwind into your Render Engine
framework as well.

## Getting Setup with Tailwind CSS
This isn't a definitive guide on how to use Tailwind CSS, rather a simple step-by-step on what is needed to add the styles to your Render Engine project.
Consult the Tailwind CSS documentation for a more in-depth look at the styling process.

You can download tailwind via npm or you can download it from source.

`npm install tailwindcss`

I would recommend via npm as you can easily implement some of the pruning
features of the build process.

Tailwind uses a config file to update the system config.js.

Here is a copy of the `tailwind.config.js` file that I have used.

```javascript
module.exports = {
  purge: {
    enabled: true,
    mode: 'all',
    content: [
      './output/**/*.html',
      './output/**/*.js',
    ],
  },
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [
    // ...
    require('tailwindcss'),
    require('autoprefixer'),
    // ...
  ],
}
```

Let's break this down bit by bit.


```javascript
  purge: {
    enabled: true,
    mode: 'all',
    content: [
      './output/**/*.html',
      './output/**/*.js',
    ],
  },
```

This makes it so that only code that is needed for your site is added to your
final css. This can transform a 22+ MB file and make only a few KB.

The one drawback to this is that you will only have access to the styles that
you have added. This can add a little confusion when editing the design. I
would suggest setting `enabled: false` until you are ready to publish to the
web.

The `content` portion of purge tells Tailwind CSS where to look for calls to the
css.

`./output/**/*.html` ensures that all html files are checked in `output`.

```javascript
  plugins: [
    // ...
    require('tailwindcss'),
    require('autoprefixer'),
    // ...
  ],
```

This loads `tailwindcss` and the `autoprefixer` that we use for the buildout.


## Build your base stylesheet

This **WON'T** be the final version that is added to the site so be sure to
name it something that is easy to recall.

```
$ touch static/pre-styles.css
```

In that file, add your tailwind components. Apply any modifications to the base
style here.

```css
@tailwind base;
// add modifications
h1 {
  @apply text-4xl;
  }

@tailwind components;
// add modifications

@tailwind utilities;
```

## Add some Tailwind CSS to your Templates

Just a quick reminder that if you have `purge: true` set, CSS will not be
generated if there are no html classes that call it. If you haven't yet, start
adding some Tailwind CSS classes to your templates.

## Generate the CSS File for Your Project

Once you have some Tailwind CSS added to your templates, you will not see the
styles work until you add the rendered stylesheet.

```html
<!-- In each file that needs it -->

<link rel="stylesheet" type="text/css" href="/static/tailwind.css">
```

You may be asking "Woah! Where did this file come from?"

The file doesn't exist yet, but we need to build the output directory prior to
adding it.

Let's run render engine.

`$ python run.py`

This will build the website as expected.

Lastly, generate the `tailwind.css` stylesheet with the `build` command.

`npx tailwindcss build pre-styles.css -o output/static/tailwind.css`

This will create the missing file and add it into your output folder.

## Autogenerate your CSS

You can add the build command into your run.py.

```python
# from run.py
from render-engine import Site, Page
import subprocess

site = Site()

@site.register_route()
class Index(Page):
    pass

... # your site code

if __name__ == "__main__":
    site.render()
    subprocess.command(['npx', 'tailwindcss', 'build', 'pre-styles.css', '-o', 'output/static/tailwind.css'])
```

## Can You Look at the Templates?

I haven't tested this but I could see that working. This would make it so that
you can build your tailwind css files into static and then have it copy over
when you render your site. Of course this could add some features based on
optionals and if you want to include styling in your `Page.content` it would
not be included. Furthermore, you would still need to run the npx build to get
any updated styles.
