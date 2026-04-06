import requests
import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from random import random


def upload_comment9(url, comment_text): # The acutal posting function
    with sync_playwright() as p:
        # 1. Setup Browser
        browser = p.chromium.launch(headless=False, slow_mo=300)
        
        # Locking viewport to 1280x800 to match your hard-coded coordinates
        context = browser.new_context(
            storage_state="auth.json", # Load saved login state
            viewport={'width': 1280, 'height': 800}
        )

        # --- VISUAL CLICK HELPER SCRIPT ---
        # This injects JavaScript to show a red dot wherever the mouse clicks
        context.add_init_script("""
            window.addEventListener('mousedown', e => {
                const dot = document.createElement('div');
                dot.style.position = 'fixed';
                dot.style.left = (e.clientX - 10) + 'px';
                dot.style.top = (e.clientY - 10) + 'px';
                dot.style.width = '20px';
                dot.style.height = '20px';
                dot.style.borderRadius = '50%';
                dot.style.background = 'rgba(255, 0, 0, 0.8)';
                dot.style.border = '2px solid white';
                dot.style.zIndex = '999999';
                dot.style.pointerEvents = 'none';
                document.body.appendChild(dot);
                setTimeout(() => dot.remove(), 1000); 
            }, true);
        """)

        page = context.new_page()

        try:
            print(f"Navigating to: {url}")
            page.goto(url, wait_until="commit", timeout=60000)

            # 2. Trigger the OpenWeb engine
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            print("Waiting for 'Join the Conversation' button...")
            cta = page.locator(cta_selector).first
            cta.wait_for(state="visible", timeout=20000)
            
            cta.scroll_into_view_if_needed()
            print("Visual Click: Triggering CTA...")
            cta.click() 
            
            # Wait for the box to slide/fade in
            time.sleep(8) 

            # 3. HARD-CODED INTERACTION (Based on your screenshot)
            target_x = 640 
            target_y = 420 + 50 + 25 + 60 - 30

            print(f"Visual Click: Targeting coordinates {target_x}, {target_y}")
            page.mouse.click(target_x, target_y)
            
            # Pause to ensure the cursor is active in the box
            time.sleep(2)

            # 4. TYPE THE COMMENT
            print("Simulating typing...")
            page.keyboard.type(comment_text, delay=20) 
            time.sleep(2)
            
            # 5. TAB AND ENTER SEQUENCE
            print("Tabbing through icons to reach Post button...")
            for i in range(5):
                page.keyboard.press("Tab")
                time.sleep(0.5)
            
            # Uncomment the line below when you are ready to go live
            page.keyboard.press("Enter")
            
            print("Sequence complete.")
            time.sleep(5) 

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()


def upload_comment8(url, comment_text): # Use this funciton for testing
    with sync_playwright() as p:
        # 1. Setup Browser
        browser = p.chromium.launch(headless=False, slow_mo=300)
        
        # Locking viewport to 1280x800 to match your hard-coded coordinates
        # context = browser.new_context(
        #     storage_state="auth.json", # Load saved login state
        #     viewport={'width': 1280, 'height': 800}
        # )

        # Testing version
        context = browser.new_context(
            viewport={'width': 1280, 'height': 800}
        )

        # --- VISUAL CLICK HELPER SCRIPT ---
        # This injects JavaScript to show a red dot wherever the mouse clicks
        context.add_init_script("""
            window.addEventListener('mousedown', e => {
                const dot = document.createElement('div');
                dot.style.position = 'fixed';
                dot.style.left = (e.clientX - 10) + 'px';
                dot.style.top = (e.clientY - 10) + 'px';
                dot.style.width = '20px';
                dot.style.height = '20px';
                dot.style.borderRadius = '50%';
                dot.style.background = 'rgba(255, 0, 0, 0.8)';
                dot.style.border = '2px solid white';
                dot.style.zIndex = '999999';
                dot.style.pointerEvents = 'none';
                document.body.appendChild(dot);
                setTimeout(() => dot.remove(), 1000); 
            }, true);
        """)

        page = context.new_page()

        try:
            print(f"Navigating to: {url}")
            page.goto(url, wait_until="commit", timeout=60000)

            # 2. Trigger the OpenWeb engine
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            print("Waiting for 'Join the Conversation' button...")
            cta = page.locator(cta_selector).first
            cta.wait_for(state="visible", timeout=20000)
            
            cta.scroll_into_view_if_needed()
            print("Visual Click: Triggering CTA...")
            cta.click() 
            
            # Wait for the box to slide/fade in
            time.sleep(8) 

            # 3. HARD-CODED INTERACTION (Based on your screenshot)
            target_x = 640 
            target_y = 420 + 50 + 25 + 60 - 30

            print(f"Visual Click: Targeting coordinates {target_x}, {target_y}")
            page.mouse.click(target_x, target_y)
            
            # Pause to ensure the cursor is active in the box
            time.sleep(2)

            # 4. TYPE THE COMMENT
            print("Simulating typing...")
            page.keyboard.type(comment_text, delay=20) 
            time.sleep(2)
            
            # 5. TAB AND ENTER SEQUENCE
            print("Tabbing through icons to reach Post button...")
            for i in range(5):
                page.keyboard.press("Tab")
                time.sleep(0.5)
            
            # Uncomment the line below when you are ready to go live
            # page.keyboard.press("Enter")
            
            print("Sequence complete.")
            time.sleep(5) 

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

def upload_comment7(url, comment_text):
    with sync_playwright() as p:
        # 1. Launch headed so you can see the magic happen
        browser = p.chromium.launch(headless=False)
        
        # CRITICAL: Lock the viewport so X,Y coordinates are consistent
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        try:
            print(f"Navigating to: {url}")
            page.goto(url, wait_until="domcontentloaded")

            # 2. Trigger the section (Required to make the box exist)
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            page.wait_for_selector(cta_selector, timeout=15000)
            page.locator(cta_selector).first.scroll_into_view_if_needed()
            page.locator(cta_selector).first.click()
            
            print("CTA Clicked. Waiting 3 seconds for animation...")
            time.sleep(3) # Wait for the box to slide/fade in

            # 3. HARD-CODED INTERACTION
            # Replace 640, 500 with the actual coordinates you found
            # (640 is center-width of 1280, 500 is roughly mid-screen)
            target_x = 640 
            target_y = 420 

            print(f"Clicking hard-coded coordinates: {target_x}, {target_y}")
            page.mouse.click(target_x, target_y)
            time.sleep(0.5)

            # 4. SIMULATED PASTE (Control+V)
            # We put the text in the clipboard and paste it
            # Or use the keyboard to type it if clipboard access is restricted
            print("Simulating Paste and Submission...")
            page.keyboard.type(comment_text, delay=20) 
            
            # 5. TAB AND ENTER
            page.keyboard.press("Tab")
            time.sleep(0.5)
            #page.keyboard.press("Enter")
            
            print("Sequence complete.")
            time.sleep(5) # Leave open to see the 'Sent' message

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

# Example:
# upload_comment("YOUR_URL", "Harris would have handled this better!")


def upload_comment6(url, comment_text):
    with sync_playwright() as p:
        # 1. High-Stealth Launch
        # We use 'channel="chrome"' if available, or just standard chromium
        browser = p.chromium.launch(headless=False, slow_mo=300) 
        
        # A very specific, modern User Agent is required
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 800}
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded")
            
            # 1. Find the CTA
            cta = page.locator('div[class*="CommentCallToAction_commentText"]').first
            cta.scroll_into_view_if_needed()
            
            # 2. Get coordinates and click like a human
            box = cta.bounding_box()
            page.mouse.click(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
            print("Clicked CTA coordinates.")

            # 3. WAIT for the iframe to be injected
            # Instead of searching for it once, we poll for 10 seconds
            comment_frame = None
            for _ in range(20): # Try for 10 seconds
                time.sleep(0.5)
                for frame in page.frames:
                    if "spot.im" in frame.url or "openweb" in frame.url:
                        comment_frame = frame
                        break
                if comment_frame: break
            
            if not comment_frame:
                # If still not found, take a screenshot to see if a Login/Ad popped up
                page.screenshot(path="no_frame_found.png")
                raise Exception("Iframe never appeared. Check no_frame_found.png")

            # 4. Once the frame exists, use the mouse to click the box INSIDE the frame
            # We need the box of the editor relative to the frame
            print("Iframe found. Entering text...")
            editor_selector = 'div[contenteditable="true"]'
            
            # We must interact WITH the frame object now
            editor = comment_frame.locator(editor_selector).first
            editor.wait_for(state="visible")
            editor.click() 
            editor.type(comment_text, delay=50)

        except Exception as e:
            print(f"Error: {e}")


def upload_comment5(url, comment_text):
    with sync_playwright() as p:
        # 1. Setup Browser
        # Set headless=False if you want to watch the browser work
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            print(f"Navigating to: {url}")
            # 'commit' is faster; we handle the loading of the comments manually
            page.goto(url, wait_until="commit", timeout=60000)

            # 2. Trigger the OpenWeb engine by clicking "Join the Conversation"
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            print("Waiting for 'Join the Conversation' button...")
            cta = page.locator(cta_selector).first
            cta.wait_for(state="visible", timeout=20000)
            
            # Scroll and click
            cta.scroll_into_view_if_needed()
            cta.click()
            print("Clicked CTA. Waiting for iframe to inject...")

            time.sleep(5) # Wait for the box to slide/fade in

            # 3. HARD-CODED INTERACTION
            # Replace 640, 500 with the actual coordinates you found
            # (640 is center-width of 1280, 500 is roughly mid-screen)
            target_x = 640 
            target_y = 420 

            print(f"Clicking hard-coded coordinates: {target_x}, {target_y}")
            page.mouse.click(target_x, target_y)
            time.sleep(5)

            # 4. SIMULATED PASTE (Control+V)
            # We put the text in the clipboard and paste it
            # Or use the keyboard to type it if clipboard access is restricted
            print("Simulating Paste and Submission...")
            page.keyboard.type(comment_text, delay=20) 
            
            # 5. TAB AND ENTER
            page.keyboard.press("Tab")
            time.sleep(0.5)
            page.keyboard.press("Tab")
            time.sleep(0.5)
            page.keyboard.press("Tab")
            time.sleep(0.5)
            page.keyboard.press("Tab")
            time.sleep(0.5)
            page.keyboard.press("Tab")
            time.sleep(0.5)
            #page.keyboard.press("Enter")
            
            print("Sequence complete.")
            time.sleep(5) # Leave open to see the 'Sent' message

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

            # # 3. Switch focus to the OpenWeb Iframe
            # # Using multiple possible selectors for the iframe to be safe
            # iframe_selector = 'iframe[title="Comments"], iframe[id*="spotim"], iframe[src*="spot.im"]'
            # page.wait_for_selector(iframe_selector, timeout=30000)
            # comment_frame = page.frame_locator(iframe_selector)

            # # 4. Target the Text Editor
            # # data-testid is the most stable selector for OpenWeb
            # editor_selector = 'div[data-testid="editor-editable"], div[aria-label="Write a comment"], div[contenteditable="true"]'
            # editor = comment_frame.locator(editor_selector).first
            
            # print("Waiting for editor to be attached...")
            # editor.wait_for(state="attached", timeout=20000)

            # # 5. FORCE FOCUS via JavaScript
            # # This bypasses "Glass Panes" (invisible overlays) that block standard clicks
            # print("Forcing focus and click via JS execution...")
            # editor.evaluate("node => { node.focus(); node.click(); }")
            
            # # Give the UI a moment to register the focus
            # page.wait_for_timeout(1000)

            # # 6. Enter the text
            # # We use type() with a small delay to simulate human typing and wake up the 'Post' button
            # print("Entering comment text...")
            # editor.type(comment_text, delay=40)

            # # 7. Submit the Comment
            # post_button_selector = 'button[data-testid="post-button"], button:has-text("Post")'
            # post_button = comment_frame.locator(post_button_selector).first
            
            # # Final check to see if the button is ready
            # post_button.wait_for(state="visible", timeout=10000)
            
            # if post_button.is_enabled():
            #     print("Clicking Post button...")
            #     post_button.click()
            #     print("Comment successfully submitted!")
            #     # Brief pause to allow the network request to complete
            #     page.wait_for_timeout(3000)
            # else:
            #     print("Post button is disabled. Trying one last 'Enter' key press...")
            #     editor.press("Enter")
            #     if post_button.is_enabled():
            #         post_button.click()
            #         print("Submitted via Enter key fallback.")
            #     else:
            #         print("Failed: Submit button stayed disabled.")

        # except Exception as e:
        #     print(f"An error occurred: {e}")
        #     page.screenshot(path="final_debug_error.png")
        #     print("Saved debug screenshot to final_debug_error.png")
        
        # finally:
        #     browser.close()

# To use this:
# upload_comment("https://komonews.com/...", "This is my automated comment.")

def upload_comment4(url, comment_text):
    with sync_playwright() as p:
        # Launching with a real user agent is non-negotiable for Sinclair sites
        browser = p.chromium.launch(headless=False, slow_mo=300) 
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            print(f"Navigating to article...")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)

            # 1. Trigger the Comment Section
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            print("Waiting for 'Join the Conversation' button...")
            cta = page.locator(cta_selector).first
            cta.wait_for(state="visible", timeout=15000)
            cta.click()
            print("CTA Clicked. Entering Iframe context...")

            # 2. Identify and Switch to the Iframe
            # OpenWeb uses 'Comments' or 'Spot.im' in the title/id
            iframe_selector = 'iframe[title="Comments"], iframe[id*="spotim"]'
            page.wait_for_selector(iframe_selector, timeout=30000)
            comment_frame = page.frame_locator(iframe_selector)

            # 3. Locate the Text Editor
            # OpenWeb's specific attribute for the editable div
            editor_selector = 'div[data-testid="editor-editable"], div[aria-label="Write a comment"]'
            editor = comment_frame.locator(editor_selector).first
            
            print("Waiting for editor to be interactable...")
            editor.wait_for(state="visible", timeout=20000)
            editor.click() # Focus the element

            # 4. Input Text (Human Simulation)
            # We use press_sequentially because .fill() can be detected/ignored
            print("Typing comment...")
            editor.press_sequentially(comment_text, delay=30)
            
            # 5. Submit the Comment
            # The 'Post' button only enables after typing
            # post_button = comment_frame.locator('button[data-testid="post-button"], button:has-text("Post")')
            # post_button.wait_for(state="visible", timeout=10000)
            
            # if post_button.is_enabled():
            #     print("Clicking Submit...")
            #     post_button.click()
            #     print("Successfully submitted!")
            #     # Wait to ensure the request clears
            #     page.wait_for_timeout(3000) 
            # else:
            #     # Fallback: Sometimes a small 'click' inside the editor is needed to wake the button
            #     print("Post button disabled, retrying focus...")
            #     editor.click()
            #     page.wait_for_timeout(1000)
            #     post_button.click()

        except Exception as e:
            print(f"Process Failed: {e}")
            page.screenshot(path="debug_final_error.png")
            print("Check debug_final_error.png to see the state of the Iframe.")
        
        finally:
            browser.close()

# Usage
# upload_comment("https://komonews.com/...", "Your text here")

def upload_comment3(url, comment_text):
    with sync_playwright() as p:
        # 1. Setup Browser (headless=False is useful for debugging)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            print(f"Navigating to: {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)

            # 2. Handle the "Join the Conversation" Button
            # We use a partial class match to avoid issues with dynamic hashes
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            print("Waiting for CTA button to be ready...")
            
            cta_button = page.locator(cta_selector).first
            cta_button.wait_for(state="visible", timeout=20000)
            
            # Click and wait for the page to react
            cta_button.click()
            print("Clicked CTA successfully. Waiting for iframe to inject...")
            
            # 3. Handle the OpenWeb Iframe
            # This is where most scripts hang. We must target the frame by title or URL.
            iframe_selector = 'iframe[title="Comments"]'
            page.wait_for_selector(iframe_selector, timeout=30000)
            
            # Create a frame locator to "enter" the iframe
            comment_frame = page.frame_locator(iframe_selector)

            # 4. Find the Text Editor inside the frame
            # OpenWeb typically uses a div with aria-label or contenteditable
            editor = comment_frame.locator('div[aria-label="Write a comment"]')
            
            print("Focusing text editor...")
            editor.wait_for(state="visible", timeout=20000)
            editor.click()
            
            # 5. Type the comment
            # press_sequentially is safer than fill() for rich text editors
            editor.press_sequentially(comment_text, delay=50)
            print(f"Comment text '{comment_text}' entered.")

            # 6. Click the Post Button
            post_button = comment_frame.locator('button:has-text("Post")')
            post_button.wait_for(state="visible", timeout=10000)
            
            if post_button.is_enabled():
                post_button.click()
                print("Submit button clicked!")
                # Give it a moment to process the post
                time.sleep(2) 
            else:
                print("Post button is disabled - text might not have registered.")

        except Exception as e:
            print(f"Error encountered: {e}")
            page.screenshot(path="debug_error.png")
            print("Detailed error screenshot saved to debug_error.png")
        
        finally:
            browser.close()

# Example Call:
# upload_comment("https://komonews.com/news/nation-world/...", "My comment text")

def upload_comment2(url, comment_text):
    with sync_playwright() as p:
        # Launch browser - set headless=False if you want to watch it work
        browser = p.chromium.launch(headless=False)
        

        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)

            # 1. Target the CTA button
            cta_selector = 'div[class*="CommentCallToAction_commentText"]'
            
            # Use a locator instead of waiting for a selector
            # Locators are 'lazy' and will re-find the element if it changes
            cta_button = page.locator(cta_selector).first
            
            print("Waiting for CTA button to be ready...")
            # Wait for it to be attached and visible
            cta_button.wait_for(state="visible", timeout=20000)
            
            # 2. Click it without explicit scrolling 
            # (Playwright clicks automatically scroll, but .click() is safer here)
            cta_button.click()
            print("Clicked CTA successfully.")

            # 3. Wait for the OpenWeb Container to ATTACH
            # We don't check for 'visible' yet because it might be 0px tall while loading
            container_selector = ".js-openWebConversation-Container_0"
            page.wait_for_selector(container_selector, state="attached", timeout=30000)
            
            # 4. TRICKY PART: The Iframe
            # OpenWeb takes a few seconds to inject the iframe AFTER the click.
            print("Waiting for OpenWeb iframe to initialize...")
            
            # We wait for the iframe itself to exist in the DOM
            page.wait_for_selector('iframe[title="Comments"]', timeout=20000)
            
            # Switch to the frame locator
            comment_frame = page.frame_locator('iframe[title="Comments"]')
            
            # 5. Find the text area inside the frame
            # OpenWeb usually uses a div with 'contenteditable'
            editor = comment_frame.locator('div[aria-label="Write a comment"]') # Alternate selector
            if not editor.count():
                editor = comment_frame.locator('div[data-testid="editor-editable"]')

            print("Entering comment text...")
            editor.wait_for(state="visible", timeout=15000)
            editor.fill(comment_text)
            
            print("Done!")

        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="debug_error.png") 

# Example usage:
# upload_comment("YOUR_URL_HERE", "Harris would have handled this better!")

def upload_comment(url, comment):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        # 1. Navigate with a less restrictive wait
        page.goto(url, wait_until="domcontentloaded")

        # 2. "Human" Scroll: OpenWeb won't load unless it thinks you are reading
        # We scroll to the bottom, then wait a moment for the script to trigger
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000) 

        # 3. Use 'attached' state instead of 'visible'
        # Sometimes the container is in the DOM but height is 0px initially
        try:
            selector = ".js-openWebConversation-Container_0"
            page.wait_for_selector(selector, state="attached", timeout=30000)
            
            # 4. Scroll the element into view specifically
            page.locator(selector).scroll_into_view_if_needed()
            
            # Proceed with your posting logic...
            print("Comment section found!")
            
        except Exception as e:
            # Debugging: Take a screenshot to see what the bot is seeing
            page.screenshot(path="debug_timeout.png")
            print(f"Failed to find comments. Check debug_timeout.png. Error: {e}")

    # with sync_playwright() as p:
    #     # links = get_article_links()
    #     # if not links:
    #     #     return "Error: No article links found"
    #     # link_to_visit = random.choice(links) # Randomly select an article to comment on
    #     browser = p.chromium.launch(headless=False, slow_mo=300)

    #     # context = browser.new_context(storage_state="auth.json")
    #     # page = context.new_page()
    #     page = browser.new_page()

    #     #page.goto(url, wait_until="networkidle") # Wait for the page to load
    #     page.goto(url, wait_until="domcontentloaded", timeout=60000)

    #     # Scroll to the bottom to trigger lazy-loading scripts
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    #     page.wait_for_selector(".js-openWebConversation-Container_0", timeout=20000) # Wait for the comment section to load
    #     page.locator("#js-CommentCallToAction-Container").scroll_into_view_if_needed() # Scroll to comment section
        
    #     comment_box = page.get_by_role("textbox", name="Write a comment") # Find the comment box
    #     comment_box.wait_for(state="visible") # Wait for the comment box to be visible
    #     comment_box.click() # Click to focus the comment box
    #     comment_box.fill(comment) # Fill in the comment
    #     #page.get_by_role("button", name="Post").click() # Click the post button
    #     browser.close()

    #     #input("Press enter to continue...") # Keep the page open until user input
    #     # page.fill("#comment-input", comment)
    #     # page.click("#submit-button")
    #     # browser.close()

# Get article links from the site (not used anymore)
# def get_article_links():
#     url = "https://komonews.com/news/nation-world"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     article_links = []
#     for a in soup.select('a[href*="/news/nation-world/"]'):
#         href = a['href']
#         if href.startswith("/news/nation-world/"):
#             article_links.append("https://komonews.com" + href)
#     return article_links

if __name__ == "__main__":
    #upload_comment("This is a test comment.")
    #upload_comment8("https://komonews.com/news/nation-world/all-hell-will-reign-down-trump-gives-iran-48-hour-ultimatum-over-strait-of-hormuz-oil-gas-gasoline-military-escalation-war-conflict-operation-epic-fury-attacks-strikes-united-states-israel-president-donald-trump-peace-talks", "Harris would have handled this better!")
    upload_comment8("https://komonews.com/news/local/man-accused-of-crashing-truck-into-taxi-killing-elderly-woman-in-seattle-re-arrested-downtown-drivers-license-illegal-investigation-treatment-facility-vehicular-homicide-prosecutors-road-traffic-safety-speeding", "Wow.  My heart goes out to the family.  Awful situation all around.")
    #get_article_links()

# #section-main-page > div.PageColumn_pageColumn__21k88 > div > div.StickyTwoColumn_leftColumn__EmK0K > div > div.SectionHeroTeasers_panel__MBG0R.Panel_panel__wT2cw > div > div.SectionHeroTeasers_heroTeaser__R9w3d > div > a > div.TeaserLink_teaserText__g1DQc > div:nth-child(2)
# all-hell-will-reign-down-trump-gives-iran-48-hour-ultimatum-over-strait-of-hormuz-oil-gas-gasoline-military-escalation-war-conflict-operation-epic-fury-attacks-strikes-united-states-israel-president-donald-trump-peace-talks

# Prompt: Based on the following article, 