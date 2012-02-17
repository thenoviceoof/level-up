level-up
================================================================================

ABOUT
--------------------------------------------------------------------------------
If you haven't read the post that inspired this, go do that:

http://jasonrudolph.com/blog/2011/08/09/programming-achievements-how-to-level-up-as-a-developer/

Now, there's a [gist attached to the article](https://gist.github.com/1133830)
that lets you fork and cross off which ones you've finished, as a sort of
self-tracking tool, but it seems to me that like many things,
*the journey is more important than the destination*.

Hence, this project.

You can see it in action [here](http://thenoviceoof.github.com/level-up/).

USAGE
--------------------------------------------------------------------------------
 * fork this repo
 * enable github pages
   * hit the admin button on your 
   * you'll probably want to `git branch -D gh-pages`
   * `git symbolic-ref HEAD refs/heads/gh-pages`
   * `rm .git/index`
   * `git clean -fdx`
   * `git merge master` to get an empty template
   * `git push origin gh-pages`
   * if that doesn't work, report it to the github issues tracker
 * change the first 5 lines of index.html
 * edit the files under all/
   * each file corresponds to a single entry
   * the three states are [todo, wip, done]
   * the entries are named in reverse display order

BUGS
--------------------------------------------------------------------------------
There will be bugs: if there are, please report them to:

    https://github.com/thenoviceoof/level-up/issues

Or fork and fix!